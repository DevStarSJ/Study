#Using async method in static constructor ( C# )

`static constructor` 내부에서 `async` 함수를 호출할 경우 제대로 동작을 하지 않습니다.  
(왠만해서는 이런식으로 code가 이루어지지 않도록 해야하지만, 어쩔수 없이 이렇게 사용해야 할 경우가 발생 할 수 있습니다.)  

* 참고로 `static constructor`는 해당 `class`가 가장 먼저 사용 될 때 실행됩니다.

### CLR-internal lock

`static constructor`는 정확히 1번만 실행되어야 합니다.  
그러므로 `static constructor`가 실행될 때는 내부적으로 `CLR-internal lock`으로 해당 code를 1번만 실행되도록 수행합니다.  
이렇게 lock이 걸린 상태에서 `async`를 이용하여 다른 `thread`로 작업을 수행할 경우 `thread-lock`과 `CLR-internal lock`간의 `deadlock`이 발생해서 안된다고 생각 할 수 있습니다.

<http://blogs.msdn.com/b/pfxteam/archive/2011/05/03/10159682.aspx> 링크의 posting을 보면 설명이 되어 있습니다.

<http://blog.stephencleary.com/2013/01/async-oop-2-constructors.html> 링크의 posting에도 절대로 `static constructor`에서 `async` 작업을 하는 건 `BAD CODE!!!`라고 경고하고 있습니다.

참고로 위 Link에 있는 posting에서 안된다고 하는 예제들을 만들어서 해보면 잘 됩니다.  
진짜로 async 한 작업 (DB, Network, disk I/O) 을 이용하는 경우에는 안 될 수 있지만, 단순히 async 키워드만 붙였다고 해서 `deadlock`이 재현되지는 않습니다.

### Deadlock in async method in static constuctor

강제로 `deadlock`을 발생시키는 code를 만들어 보았습니다.

```C#
using System.Collections.Generic;
using System.Threading.Tasks;

class StaticClass
{
    public static IEnumerable<string> Names { set; get; }

    static StaticClass()
    {
        Names = Task.Run(async () => { return await GetNamesAsync(); }).Result;
    }

    public static async Task<IEnumerable<string>> GetNamesAsync()
    {
        List<string> nameList = new List<string>
        {
            "Luna", "Star", "Philip"
        };

        return nameList;
    }
}

class Program
{
    static void Main(string[] args)
    {
        foreach (string name in StaticClass.Names)
        {
            System.Console.WriteLine(name);
        }
    }
}
```

이런 code를 어떻게 고쳐야 하는지 3가지 방법을 살펴보겠습니다.

###1. async한 구현의 method를 추가

위 예제의 경우 `GetNamesAsync()` method와 같은 기능을 하는 sync한 metho인 `GetNames()`를 추가하는 방법이 있습니다.  
동일한 구현이 2개가 되므로 별로 추천드리는 방법은 아닙니다.  

참고로 아래 예제도 썩 그렇게 좋은 예제코드는 아닙니다.

```C#
using System.Collections.Generic;
using System.Threading.Tasks;

class StaticClass
{
    public static IEnumerable<string> Names { set; get; }

    static StaticClass()
    {
        Names = GetNames();
    }

    public static async Task<IEnumerable<string>> GetNamesAsync()
    {
        List<string> nameList = new List<string>
        {
            "Luna", "Star", "Philip"
        };

        return nameList;
    }

    public static IEnumerable<string> GetNames()
    {
        List<string> nameList = new List<string>
        {
            "Luna", "Star", "Philip"
        };

        return nameList;
    }
}

class Program
{
    static void Main(string[] args)
    {
        foreach (string name in StaticClass.Names)
        {
            System.Console.WriteLine(name);
        }
    }
}
```

하지만 sync한 작업으로 구현 자체가 될 것을 굳이 `async`로 선언할 일은 잘 없습니다.  
그러므로 이렇게 해결될 수 있는 일이라면 애초에 `async`로 구현한거 자체가 제대로 된 설계가 아닐 수 있습니다.

###2. async 작업을 별도 class로 분리 (또는 async 작업 호출을 별도 class로 제한)

`async` 작업을 별도 class로 분리하거나,
`static constructor`에서 호출하는 `async` 작업을 다른 class의 method로 제한하는 방법이 있습니다.  
이렇게 구현할 경우 원래 `class`에서 sync한 구현과 async한 구현이 모두 필요할 경우 1번과 같은 code 모양이 될 경우가 많습니다.  
`static constructor`에서 호출하는 `async method`가 다른 class의 method일 경우에는 `deadlock`이 걸리지 않았습니다.  

```C#
using System.Collections.Generic;
using System.Threading.Tasks;

class StaticClass
{
    public static IEnumerable<string> Names { set; get; }

    static StaticClass()
    {
        Names = GetNames();
    }

    public static IEnumerable<string> GetNames()
    {
        return Task.Run(async () => { return await AsyncClass.GetNamesAsync(); }).Result; ;
    }
}

class AsyncClass
{
    public static async Task<IEnumerable<string>> GetNamesAsync()
    {
        List<string> nameList = new List<string>
        {
            "Luna", "Star", "Philip"
        };

        return nameList;
    }
}

class Program
{
    static void Main(string[] args)
    {
        foreach (string name in StaticClass.Names)
        {
            System.Console.WriteLine(name);
        }
    }
}
```

###3. 초기화 작업을 별도 Init method로 분리

개인적으로 이 방법이 가장 깔끔해 보입니다.  
해당 `class`가 사용되기 전에 `Init()`을 호출한 뒤에 사용하면 됩니다.  
`Init()`함수가 호출되기 전에 이미 해당 `class`의 `static constructor`가 실행된 상태이기 때문에 `CLR-internal lock`은 이미 `unlcok`된 상태에서 `async`작업을 수행하게 됩니다.    
하지만 여러 thread에서 `Init()` 함수가 호출될 가능성이 있을 경우에는 사용자가 별도로 `lock`을 걸어서 호출을 해야 합니다.  
해당 기능은 `clsss`가 최초로 사용되기 이전 시점의 아무 곳에서나 호출이 가능하므로, `lock`이 필요없는 적당한 시점에 호출시켜 주는 것이 좋습니다.  

```C#
using System.Collections.Generic;
using System.Threading.Tasks;

class StaticClass
{
    public static IEnumerable<string> Names { set; get; }

    static StaticClass()
    {
        ...
    }

    public static void Init()
    {
        Names = Task.Run(async () => { return await GetNamesAsync(); }).Result;
    }

    public static async Task<IEnumerable<string>> GetNamesAsync()
    {
        List<string> nameList = new List<string>
        {
            "Luna", "Star", "Philip"
        };

        return nameList;
    }
}

class Program
{
    static void Main(string[] args)
    {
        StaticClass.Init();
        foreach (string name in StaticClass.Names)
        {
            System.Console.WriteLine(name);
        }
    }
}
```




