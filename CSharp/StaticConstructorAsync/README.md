#Using async method in static constructor ( C# )

`static constructor` 내부에서 `async` 함수를 호출할 경우 제대로 동작을 하지 않습니다.  
(왠만해서는 이런식으로 code가 이루어지지 않도록 해야하지만, 어쩔수 없이 이렇게 사용해야 할 경우가 발생 할 수 있습니다.)  

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






