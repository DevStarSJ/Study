# 명명규칙

## 여러가지 명명규칙이 혼용되며 사용 기준이 불명확합니다.
1. 지역 변수
> `R_TreeNode`, `xml`, `ChildXmlNode`, ...

1. 필드
> `Trans`, `sql_instance`, ...

1. 메서드
> `Begin()`(동사), `Transaction()`(명사), ...

## 식별자의 설명력이 부족합니다.
1. `public int MENU_Tree(...)`
> 메서드가 무슨 기능을 하며 반환 값이 어떤 의미를 가지는지 파악하기 어렵습니다.

1. `public int MENU_NavTreeView(TreeView P_TreeView, XmlNode P_XmlNode)`
> 매개변수 `P_TreeView`와 `P_XmlNode`는 형식 이름에 `P_` 접두사가 붙은 것으로 보이며 메서드 매개변수로서 어떤 역할을 하는지 두 변수 사이에 어떤 관계가 있는지 표현하지 못합니다.

# 방어구문 부족
매개변수에 대한 방어구문(guard clauses)이 많이 부족합니다. 방어구문을 보강하거나 방어구문을 최소화할 수 있는 디자인을 적용해야합니다.

# SQL 주입 가능성
웹 응용프로그램이 아니더라도 일반 문자열 조합을 SQL 쿼리 작성에 사용하는 것은 치명적 오류의 가능성을 열어두는 것입니다. 악의가 없더라도 프로그래머의 실수로 인해 실행되지 말아야할 명령이 실행될 수 있습니다.  다음과 유사한 'Value Object'들을 제공하는 것으로 기존 클라이언트 코드 수정을 최소하하며 예상치 못한 주입을 일관성 있게 막을 수 있습니다.

```csharp
public sealed class ColumnName
{
    private readonly string _safeColumnName;
    
    public ColumnName(string source)
    {
        if (source == null)
            throw new ArgumentNullException(nameof(source));
            
        if ... // 기타 검증 논리
            
        _safeColumnName = ... // Replace 등의 가공 논리
    }
    
    public override ToString() => _safeColumnName;
    
    public static implicit operator ColumnName(string s)
    {
        return new ColumnName(s);
    }
}

public sealed class ConditionValue
{
    private readonly string _safeConditionValue;
    
    public ConditionValue(string source)
    {
        if (source == null)
            throw new ArgumentNullException(nameof(source));
            
        if ... // 기타 검증 논리
            
        _safeConditionValue = ... // Replace 등의 가공 논리
    }
    
    public override ToString() => _safeConditionValue;
    
    public static implicit operator ConditionValue(string s)
    {
        return new ConditionValue(s);
    }
}

protected void CheckCondition(ref string SQL, ref bool IsFirst, ColumnName Col, ConditionValue Value)
{
    if (Value == "") return;

    if (IsFirst)
    {
        IsFirst = false;
        SQL += " WHERE ";
    }
    else
        SQL += " AND ";

    SQL += string.Format("{0} = '{1}' ", Col, Value);
}

CheckCondition(ref sql, ref isFirst, "MyColumn", "Hello World");
CheckCondition(ref sql, ref isFirst, "MyColumn", "Hello World' OR '' = '"); // Injection! ConditionValue 생성자의 방어구문에 의해 SQL문이 실행되기 전에 런타임 오류
```

# 정적 형식 오용
`ConnectionManager` 클래스는 정적 멤버만을 가지지만 정적 클래스가 아니기 때문에 불필요한 인스턴스를 생성할 수 있는 경로를 열어주고 있습니다.

# 캡슐화 누락
`ConnectionManager` 클래스는 필드를 방어논리 없이 직접적으로 공개하고 있습니다. 클라이언트 코드는 항상 이 필드가 안전한지 검사해야하는 부담을 가지게되며 검증 코드는 분산되고 중복되어 유지보수성을 저하시킵니다.

# 스레드 위험성
`ConnectionManager` 클래스의 공용 필드는 스레드 안정성을 보장하지 않습니다. 스레드 풀 등이 사용되면 위험합니다. 특히 'ConnectionList'는 자료구조이기 때문에 더욱 위험합니다.

# 불필요한 비생성자를 통한 개체 초기화
`ConnectionElement` 클래스는 `Constructor`라는 이름의 초기화 메서드를 가집니다. 문법적으로 불가피한 경우에 선택할 수 있지만 이미 초기화된 개체를 대상으로 호출되는 것이 문법적으로 가능성하고 불변(immutable) 개체를 초기화할 수 없기 때문에 가능하면 피하는 것이 좋습니다. 다음의 코드처럼 생성자를 이용할 수 있습니다.

```csharp
private static readonly int _defaultPort = 1234;

private readonly string _userName;
private readonly string _password;
private readonly int _port;

public Connection(string userName, string password, int port)
{
    if (userName == null)
        throw new ArgumentNullException(nameof(userName));
    if (password == null) 
        hrow new ArgumentNullException(nameof(password));
    
    _userName = userName;
    _password = password;
    _port = port;
}

public Connection(string userName, string password)
    : this(userName, password, port: _defaultPort)
{
}
```

# 봉인(sealed)되지 않은 클래스의 dispose 패턴 적용
상속 가능한 클래스가 `IDisposable` 인터페이스를 구현할 때에는 하위 클래스를 위해 dispose 패턴을 적용해야합니다.
> https://msdn.microsoft.com/en-us/library/b1yfkh5e.aspx

# 목적이 불분명한 `try-catch` 구문
다음 `try-catch` 구문은 목적이 불분명합니다.

```csharp
try
{
}
catch (MySqlException)
{
    throw;
}
```

`MySqlException` 형식의 예외에 대한 별도의 논리를 제공하지 않기 때문에 불필효한 코드입니다.

# 예외 피드백 유지
예외 개체는 예외 상황에 대한 정보를 기록합니다. 따라서 예외를 `catch`한 뒤 새로운 예외를 던져야할 때 소스 예외를 `innerException`으로 보관하는 것이 프로그래머에게 오류 상황에 대한 피드백을 최대한 전달하는 방법입니다.

```csharp
try
{
}
catch (Exception ex)
{
    throw new Exception(ex.Message.ToString());
    // 오류 소스에 대한 호출 스택을 잃어버입니다.
    // 다음과 같이 하면 피드백 품질을 유지할 수 있습니다.
    // throw new AggregationException("custom message", ex);
}
```
