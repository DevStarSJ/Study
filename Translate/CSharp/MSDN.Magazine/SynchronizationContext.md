원본 : <https://msdn.microsoft.com/en-us/magazine/gg598924.aspx>

FEBRUARY 2011 VOLUME 26 NUMBER 02

#병렬 컴퓨팅 - SynchronizationContext에 관한 모든것

>#Parallel Computing - It's All About the SynchronizationContext

By [Stephen Cleary](https://msdn.microsoft.com/en-us/magazine/mt149362?author=stephen+cleary) | February 2011

멀티 스레드 프로그래밍은 매우 어렵습니다.
제대로 이해하기 위해서는 어마어마한 양의 개념과 도구들을 학습해야 합니다.
**Microsoft .NET Framework**은 `SynchronizationContext` 클래스를 제공 합니다. 
불행히도, 많은 개발자들이 이 유용한 도구를 모르고 있습니다.

>Multithreaded programming can be quite difficult, and there’s a tremendous body of concepts and tools to learn when one embarks on this task. To help out, the Microsoft .NET Framework provides the SynchronizationContext class. Unfortunately, many developers aren’t even aware of this useful tool.

플랫폼에 상관없이 (ASP. NET, Windows Presentation Foundation, Windows 폼 (WPF), Silverlight 등) 
.NET 프로그램에는 `SynchronizationContext`의 개념이 포함 되어 있으므로,
다중 스레드를 개발할 경우 `SynchronizationContext`를 이해하고 활용할 수 있는 해택을 누릴 수 있습니다.

>Regardless of the platform—whether it’s ASP.NET, Windows Forms, Windows Presentation Foundation (WPF), Silverlight or others—all .NET programs include the concept of SynchronizationContext, and all multithreading programmers can benefit from understanding and applying it.

##**SynchronizationContext**에 대한 필요성

>##The Need for SynchronizationContext

다중 스레드 프로그램은 **.NET Framework**가 등장하기 훨씬 이전부터 있었습니다.
이 경우 한 스레드에서 다른 스레드로 작업을 전송해야 할 경우가 종종 있습니다.
Windows 프로그램은 **메시지 루프**를 중심으로 동작하기 때문에,
많은 개발자들은 **윈도우 메시지 큐**로 작업을 전달했습니다.
**윈도우 메세지 큐**에서 처리가능한 형태로 **사용자정의 윈도우 메세지**를 정의하여야 했습니다.

>Multithreaded programs existed well before the advent of the .NET Framework. These programs often had the need for one thread to pass a unit of work to another thread. Windows programs were centered on message loops, so many programmers used this built-in queue to pass units of work around. Each multithreaded program that wanted to use the Windows message queue in this fashion had to define its own custom Windows message and convention for handling it.

.NET Framework가 처음 나왔을 때에는 이런 식의 방법이 표준이었습니다.
그땐 .NET이 지원하는 GUI 어플리케이션은 **Windows Form** 뿐 이었습니다.
그러나, 프레임워크 개발자는 다른 방식의 등장을 예상하고, 범용 솔루션을 개발했습니다.
그래서 탄생한 것이 `ISynchronizeInvoke`입니다.

>When the .NET Framework was first released, this common pattern was standardized. At that time, the only GUI application type that .NET supported was Windows Forms. However, the framework designers anticipated other models, and they developed a generic solution. ISynchronizeInvoke was born.

ISynchronizeInvoke의 기본 개념은 다음과 같습니다.
"소스" 스레드는 "타겟" 스레드에서 `delegate`를 큐에 추가하고
필요에 따라 해당 `delegate`의 작업이 끝나기를 기다리게 하는 것입니다.
`ISynchronizeInvoke` 역시 "현재 코드"가 "타겟 스레드"에서 실행되고 있는지 여부를 판단할 수 있는 속성이 제공됩니다.
(이미 실행 중인 경우 `delegate`를 큐에 저장할 필요가 없습니다).
 **Windows Form**은 `ISynchronizeInvoke`를 이용한 구현만을 제공하고,
그 패턴은 비동기 구성 요소를 설계하기 위해 개발되었으므로,
전혀 문제가 되지 않았습니다.

>The idea behind ISynchronizeInvoke is that a “source” thread can queue a delegate to a “target” thread, optionally waiting for that delegate to complete. ISynchronizeInvoke also provided a property to determine whether the current code was already running on the target thread; in this case, queuing up the delegate would be unnecessary. Windows Forms provided the only implementation of ISynchronizeInvoke, and a pattern was developed for designing asynchronous components, so everyone was happy.

**.NET Framework 2.0**에는 전면적인 변경사항들이 포함되었습니다.
주요 개선점 중 하나는 **ASP.NET**에서 **비동기 페이지** 구현이 가능해 졌습니다.
**.NET Framework 2.0** 이전에는 모든 **ASP.NET** `request`는 완료 될 때까지 스레드를 가지고 있어야 했습니다.
참 비효율적이었죠.
왜냐면 웹 페이지를 만드는 과정에서 **데이터베이스 쿼리**나 **웹 서비스 호출**을 사용하는 경우가 많고,
웹 페이지 생성 `request`를 처리하는 스레드는 작업이 완료 될 때까지 기다려야 합니다.
비동기 페이지에서는 `request`를 처리하는 스레드는 각각의 작업을 시작한 다음 **ASP.NET 스레드 풀**로 반환됩니다.
작업이 완료되면 **ASP.NET 스레드 풀**의 아무 스레드에서든 해당 `request`를 완료할 수 있습니다.

>Version 2.0 of the .NET Framework contained many sweeping changes. One of the major improvements was introducing asynchronous pages to the ASP.NET architecture. Prior to the .NET Framework 2.0, every ASP.NET request needed a thread until the request was completed. This was an inefficient use of threads, because creating a Web page often depends on database queries and calls to Web services, and the thread handling that request would have to wait until each of those operations finished. With asynchronous pages, the thread handling the request could begin each of the operations and then return back to the ASP.NET thread pool; when the operations finished, another thread from the ASP.NET thread pool would complete the request.

그러나 `ISynchronizeInvoke`는 **ASP.NET 비동기 페이지 구조**에는 적합하지 않았습니다.
`ISynchronizeInvoke` 패턴을 사용하여 개발한 비동기 구성요소는 **ASP.NET** 페이지에서는 제대로 작동하지 않습니다.
비동기 페이지는 큐에 있는 작업을 원래 스레드로 전달하는 대신에, 페이지 `request` 작업을 완료할 수 있다고 판단되는 작업들의 수만 관리하면 됩니다.
그래서 많이 심사숙고한 결과, `SynchronizationContext`가 `ISynchronizeInvoke`를 대체하게 되었습니다.

>However, ISynchronizeInvoke wasn’t a good fit for the ASP.NET asynchronous pages architecture. Asynchronous components developed using the ISynchronizeInvoke pattern wouldn’t work correctly within ASP.NET pages because ASP.NET asynchronous pages aren’t associated with a single thread. Instead of queuing work to the original thread, asynchronous pages only need to maintain a count of outstanding operations to determine when the page request can be completed. After much thought and careful design, ISynchronizeInvoke was replaced by SynchronizationContext.

##`SynchronizationContext`의 개념

>##The Concept of SynchronizationContext

`ISynchronizeInvoke`에는 2가지 요구조건이 있는데,
동기화가 필요한지 판단 가능한지와
스레드 간의 작업을 queue로 전달가능하냐는 것입니다.
`SynchronizationContext`는 `ISynchronizeInvoke`를 대체하려고 만들었지만 설계하는 과정에서 완벽하게 대체하지 못하도록 바뀌었습니다.

>ISynchronizeInvoke satisfied two needs: determining if synchronization was necessary, and queuing a unit of work from one thread to another. SynchronizationContext was designed to replace ISynchronizeInvoke, but after the design process, it turned out to not be an exact replacement.

`SynchronizationContext`의 첫번째 특징은 큐에 있는 작업을 `context`에 재공한다는 것입니다.
(특정 스레드가 아닌 `context`에 제공을 한다는게 중요합니다.)
`SynchronizationContext`의 구현이 특정한 하나의 스레드에 연결되지 않으므로 그 차이는 매우 중요합니다.
`SynchronizationContext`는 동기화 필요여부를 판단하는 방법을 가지지 않는데, 왜냐면 그 판단이 항상 가능한 것은 아니기 때문입니다.

>One aspect of SynchronizationContext is that it provides a way to queue a unit of work to a context. Note that this unit of work is queued to a context rather than a specific thread. This distinction is important, because many implementations of SynchronizationContext aren’t based on a single, specific thread. SynchronizationContext does not include a mechanism to determine if synchronization is necessary, because this isn’t always possible.

두 번째 특징은 모든 스레드는 `"current" context`를 가진다는 것입니다.
그 `context`가 반드시 `unique`할 필요는 없으며 다른 스레드와 공유할 수도 있습니다.
드물긴 하지만, 스레드가 `current context`를 변경하는 것도 가능합니다.

>Another aspect of SynchronizationContext is that every thread has a “current” context. A thread’s context isn’t necessarily unique; its context instance may be shared with other threads. It’s possible for a thread to change its current context, but this is quite rare.

세 번째 특징은 완료되지 않은 비동기 작업의 수를 제한한다는 것입니다.
그러므로 ASP.NET 비동기 페이지 사용나 이런 종류의 작업 수 제한이 필요로하는 다른 호스트에서 사용이 가능합니다.
대부분의 경우 `SynchronizationContext`가 발생하면 `count`는 증가하며, 작업이 끝났다고 `context`에게 통보하면서 감소합니다.

>A third aspect of SynchronizationContext is that it keeps a count of outstanding asynchronous operations. This enables the use of ASP.NET asynchronous pages and any other host needing this kind of count. In most cases, the count is incremented when the current SynchronizationContext is captured, and the count is decremented when the captured SynchronizationContext is used to queue a completion notification to the context.

다른 특징들도 있으나, 개발자 입장에서 그다지 고려할 필요가 없습니다.
가장 중요한 특징에 대해서는 아래 **그림 1**로 표현하였습니다.

>There are other aspects of SynchronizationContext, but they’re less important to most programmers. The most important aspects are illustrated in Figure 1.

####그림 1. `SynchronizationContext` API의 주요 특징
```C#
class SynchronizationContext
{
  // context에 작업을 전달
  void Post(..); // (비동기)
  void Send(..); // (동기)

  // 비동기 작업 수를 계산
  void OperationStarted();
  void OperationCompleted();

  // 각각의 스레드는 current context를 가짐
  // "Current"가 null이면 "new SynchronizationContext()"

  static SynchronizationContext Current { get; }
  static void SetSynchronizationContext(SynchronizationContext);
}
```

>####Figure 1 Aspects of the SynchronizationContext API

```C#
class SynchronizationContext
{
  // Dispatch work to the context.
  void Post(..); // (asynchronously)
  void Send(..); // (synchronously)

  // Keep track of the number of asynchronous operations.
  void OperationStarted();
  void OperationCompleted();

  // Each thread has a current context.
  // If "Current" is null, then the thread's current context is
  // "new SynchronizationContext()", by convention.

  static SynchronizationContext Current { get; }
  static void SetSynchronizationContext(SynchronizationContext);
}
```

##`SynchronizationContext` 구현

>##The Implementations of SynchronizationContext

`SynchronizationContext`의 실제 "context"를 명확하게 정의하긴 힘듭니다.
각각의 프레임워크와 호스트에서 그들만의 `context`를 정의할 수 있습니다.
이런 구현과 한계에 관한 차이점을 정확하게 이해하는 것이 `SynchronizationContext`이 보장하는 것과 보장해 주지 않는 것에 대해서 명확하게 이해하는데 도움이 됩니다.
이 각각의 차이점에 대해서 간략하게 살펴보도록 하겠습니다.

>The actual “context” of the SynchronizationContext isn’t clearly defined. Different frameworks and hosts are free to define their own context. Understanding these different implementations and their limitations clarifies exactly what the SynchronizationContext concept does and doesn’t guarantee. I’ll briefly discuss some of these implementations.

###WindowsFormsSynchronizationContext
**(System.Windows.Forms.dll: System.Windows.Forms)**

윈도우 앱은 UI 컨트럴을 다루는 스레드의 `current context`로 `WindowsFormsSynchronizationContext`를 생성합니다.
`WindowsFormsSynchronizationContext`는 UI 컨트럴용으로 `ISynchronizeInvoke` 메서드를 사용합니다.
`ISynchronizeInvoke` 메서드는 `Win32 메세지 루프`로 `delegate`를 전달하는 역할을 수행합니다
`WindowsFormsSynchronizationContext`의 `context`는 단일 UI 스레드 입니다.

>Windows Forms apps will create and install a WindowsFormsSynchronizationContext as the current context for any thread that creates UI controls. This SynchronizationContext uses the ISynchronizeInvoke methods on a UI control, which passes the delegates to the underlying Win32 message loop. The context for WindowsFormsSynchronizationContext is a single UI thread.

`WindowsFormsSynchronizationContext` 큐에 등록된 모든 `delegate`는 한 번에 하나씩 실행됩니다.
따라서 큐에 추가된 순서대로 특정 UI 스레드에서 실행 됩니다.
각각의 UI 스레드 별로 `WindowsFormsSynchronizationContext`를 하나씩 만듭니다.

>All delegates queued to the WindowsFormsSynchronizationContext are executed one at a time; they’re executed by a specific UI thread in the order they were queued. The current implementation creates one WindowsFormsSynchronizationContext for each UI thread.

###DispatcherSynchronizationContext
(WindowsBase.dll: System.Windows.Threading)

WPF와 실버라이트 앱은 `DispatcherSynchronizationContext`를 사용하는데,
그것은 `delegate`를 UI 스레드의 디스패처에게 "일반적인" 우선순위로 큐를 통해 전달합니다.
이 `SynchronizationContext`는 `Dispatcher.Run`을 통해 스레드가 디스패처 루프를 시작할때 `current context`처럼 설정됩니다.
`DispatcherSynchronizationContext`의 `context`는 단일 UI 스레드입니다.

>WPF and Silverlight applications use a DispatcherSynchronizationContext, which queues delegates to the UI thread’s Dispatcher with “Normal” priority. This SynchronizationContext is installed as the current context when a thread begins its Dispatcher loop by calling Dispatcher.Run. The context for DispatcherSynchronizationContext is a single UI thread.

`DispatcherSynchronizationContext` 큐에 등록된 모든 `delegate`는 등록된 순서대로 한 번에 하나씩 UI 스레드에서 실행됩니다.
각각의 최상위 Window 마다 하나의 `DispatcherSynchronizationContext`를 만듭니다.
(모든 최상위 Windows가 같은 Dispatcher를 공유 하는 경우에도 마찬가지입니다.)

>All delegates queued to the DispatcherSynchronizationContext are executed one at a time by a specific UI thread in the order they were queued. The current implementation creates one DispatcherSynchronizationContext for each top-level window, even if they all share the same underlying Dispatcher.

###Default (ThreadPool) SynchronizationContext
(mscorlib.dll: System.Threading)

`SynchronizationContext`이 기본입니다.
스래드의 현재 `SynchronizationContext`가 `null`인 경우 기본 `SynchronizationContext`를 가집니다.

>The default SynchronizationContext is a default-constructed SynchronizationContext object. By convention, if a thread’s current SynchronizationContext is null, then it implicitly has a default SynchronizationContext.

기본 `SynchronizationContext`는 비동기 `delegate`는 ThreadPool에 등록하고, 동기 `delegate`는 호출 스레드에서 직접 실행 합니다.
따라서 그 `context`는 `Send`를 실행한 스레드 만큼이나 모든 ThreadPool의 스레드를 대상으로 합니다.
`context`는 `Send`를 실행한 스레드를 "빌려서" `delegate`가 완료될때까지 `context` 내부에서 사용합니다.
즉, 기본 `context`는 프로세스 상의 어떤 스레드에서도 실행 될 수 있습니다.

>The default SynchronizationContext queues its asynchronous delegates to the ThreadPool but executes its synchronous delegates directly on the calling thread. Therefore, its context covers all ThreadPool threads as well as any thread that calls Send. The context “borrows” threads that call Send, bringing them into its context until the delegate completes. In this sense, the default context may include any thread in the process.

기본 SynchronizationContext는 ASP.NET에서 호스팅하지 않는 경우 ThreadPool의 스레드에 적용됩니다.
기본 SynchronizationContext는 자식 스레드가 따로 `SynchronizationContext`를 설정하지 않은 경우 (Thread 클래스의 인스턴스가 아니라) 자식 스레드에 적용됩니다.
자식 스레드가 자신의 SynchronizationContext에를 설정하지 않으면 기본 SynchronizationContext에 또한 암시 적으로 명시 적 자식 스레드 (Thread 클래스의 인스턴스)에 적용됩니다.
그리고, UI 앱은 보통 2개의 동기 `context`를 사용합니다.
`UI SynchronizationContext`는 UI 스레드를 동작시키며, 기본 `SynchronizationContext`는 ThreadPool 스레드를 수용합니다.

>The default SynchronizationContext is applied to ThreadPool threads unless the code is hosted by ASP.NET. The default SynchronizationContext is also implicitly applied to explicit child threads (instances of the Thread class) unless the child thread sets its own SynchronizationContext. Thus, UI applications usually have two synchronization contexts: the UI SynchronizationContext covering the UI thread, and the default SynchronizationContext covering the ThreadPool threads.

기본 `SynchronizationContext`에서는 이벤트 기반 비동기 요소들이 거의 제대로 작동하지 않습니다.
대표적인 예로 UI 앱에서 백그라운드 작업이 다른 백그라운드 작업을 시작하는 것을 들 수 있습니다.
각 백그라운드 작업은 `RunWorkerAsync`를 호출하는 스레드의 `SynchronizationContext`에 의해서 동작하고, 그 후에 해당 `context`안에서 `RunWorkerCompleted event`를 실행합니다.
UI 작업용 `SynchronizationContext`인 경우에는 대게 백그라운드 작업이 하나여서, `RunWorkerAsync`로 획득한 UI `context`가 `RunWorkerCompleted`를 실행합니다. (그림 2 참고)

>Many event-based asynchronous components don’t work as expected with the default SynchronizationContext. An infamous example is a UI application where one BackgroundWorker starts another BackgroundWorker. Each BackgroundWorker captures and uses the SynchronizationContext of the thread that calls RunWorkerAsync and later executes its RunWorkerCompleted event in that context. In the case of a single BackgroundWorker, this is usually a UI-based SynchronizationContext, so RunWorkerCompleted is executed in the UI context captured by RunWorkerAsync (see Figure 2).

![image: A Single BackgroundWorker in a UI Context](https://github.com/DevStarSJ/Study/blob/master/Translate/CSharp/MSDN.Magazine/image/SynchronizationContext.01.jpg?raw=true)

####그림 2 UI `Context`에 백그라운드 작업이 하나인 경우

>####Figure 2 A Single BackgroundWorker in a UI Context

However, if the BackgroundWorker starts another BackgroundWorker from its DoWork handler, then the nested BackgroundWorker doesn’t capture the UI SynchronizationContext. DoWork is executed by a ThreadPool thread with the default SynchronizationContext. In this case, the nested RunWorkerAsync will capture the default SynchronizationContext, so it will execute its RunWorkerCompleted on a ThreadPool thread instead of a UI thread (see Figure 3).

![image: Nested BackgroundWorkers in a UI Context](https://github.com/DevStarSJ/Study/blob/master/Translate/CSharp/MSDN.Magazine/image/SynchronizationContext.02.jpg?raw=true)

####Figure 3 Nested BackgroundWorkers in a UI Context

By default, all threads in console applications and Windows Services only have the default SynchronizationContext. This causes some event-based asynchronous components to fail. One solution for this is to create an explicit child thread and install a SynchronizationContext on that thread, which can then provide a context for these components. Implementing a SynchronizationContext is beyond the scope of this article, but the ActionThread class of the Nito.Async library (nitoasync.codeplex.com) may be used as a general-purpose SynchronizationContext implementation.

###AspNetSynchronizationContext
(System.Web.dll: System.Web [internal class]) The ASP.NET SynchronizationContext is installed on thread pool threads as they execute page code. When a delegate is queued to a captured AspNetSynchronizationContext, it restores the identity and culture of the original page and then executes the delegate directly. The delegate is directly invoked even if it’s “asynchronously” queued by calling Post.

Conceptually, the context of AspNetSynchronizationContext is complex. During the lifetime of an asynchronous page, the context starts with just one thread from the ASP.NET thread pool. After the asynchronous requests have started, the context doesn’t include any threads. As the asynchronous requests complete, the thread pool threads executing their completion routines enter the context. These may be the same threads that initiated the requests but more likely would be whatever threads happen to be free at the time the operations complete.

If multiple operations complete at once for the same application, AspNetSynchronizationContext will ensure that they execute one at a time. They may execute on any thread, but that thread will have the identity and culture of the original page.

One common example is a WebClient used from within an asynchronous Web page. DownloadDataAsync will capture the current SynchronizationContext and later will execute its DownloadDataCompleted event in that context. When the page begins executing, ASP.NET will allocate one of its threads to execute the code in that page. The page may invoke DownloadDataAsync and then return; ASP.NET keeps a count of the outstanding asynchronous operations, so it understands that the page isn’t complete. When the WebClient object has downloaded the requested data, it will receive notification on a thread pool thread. This thread will raise DownloadDataCompleted in the captured context. The context will stay on the same thread but will ensure the event handler runs with the correct identity and culture.

###Notes on SynchronizationContext Implementations

SynchronizationContext provides a means for writing components that may work within many different frameworks. BackgroundWorker and WebClient are two examples that are equally at home in Windows Forms, WPF, Silverlight, console and ASP.NET apps. However, there are some points that must be kept in mind when designing such reusable components.

Generally speaking, SynchronizationContext implementations aren’t equality-comparable. This means that there’s no equivalent to ISynchronizeInvoke.InvokeRequired. However, this isn’t a tremendous drawback; code is cleaner and easier to verify if it always executes within a known context instead of attempting to handle multiple contexts.

Not all SynchronizationContext implementations guarantee the order of delegate execution or synchronization of delegates. The UI-based SynchronizationContext implementations do satisfy these conditions, but the ASP.NET SynchronizationContext only provides synchronization. The default SynchronizationContext doesn’t guarantee either order of execution or synchronization.

There isn’t a 1:1 correspondence between SynchronizationContext instances and threads. The WindowsFormsSynchronizationContext does have a 1:1 mapping to a thread (as long as SynchronizationContext.CreateCopy isn’t invoked), but this isn’t true of any of the other implementations. In general, it’s best to not assume that any context instance will run on any specific thread.

Finally, the SynchronizationContext.Post method isn’t necessarily asynchronous. Most implementations do implement it asynchronously, but AspNetSynchronizationContext is a notable exception. This may cause unexpected re-entrancy issues. A summary of these different implementations can be seen in Figure 4.

####Figure 4 Summary of SynchronizationContext Implementations

|                 | Specific Thread Used to Execute Delegates | Exclusive (Delegates Execute One at a Time) | Ordered (Delegates Execute in Queue Order) | Send May Invoke Delegate Directly | Post May Invoke Delegate Directly |
|-----------------|-------------------------------------------|---------------------------------------------|--------------------------------------------|-----------------------------------|-----------------------------------|
| Windows Forms   | Yes                                       | Yes                                         | Yes                                        | If called from UI thread          | Never                             |
| WPF/Silverlight | Yes                                       | Yes                                         | Yes                                        | If called from UI thread          | Never                             |
| Default         | No                                        | No                                          | No                                         | Always                            | Never                             |
| ASP.NET         | No                                        | Yes                                         | No                                         | Always                            | Always                            |

##AsyncOperationManager and AsyncOperation

The AsyncOperationManager and AsyncOperation classes in the .NET Framework are lightweight wrappers around the SynchronizationContext abstraction. AsyncOperationManager captures the current SynchronizationContext the first time it creates an AsyncOperation, substituting a default SynchronizationContext if the current one is null. AsyncOperation posts delegates asynchronously to the captured SynchronizationContext.

Most event-based asynchronous components use AsyncOperationManager and AsyncOperation in their implementation. These work well for asynchronous operations that have a defined point of completion—that is, the asynchronous operation begins at one point and ends with an event at another. Other asynchronous notifications may not have a defined point of completion; these may be a type of subscription, which begins at one point and then continues indefinitely. For these types of operations, SynchronizationContext may be captured and used directly.

New components shouldn’t use the event-based asynchronous pattern. The Visual Studio asynchronous Community Technology Preview (CTP) includes a document describing the task-based asynchronous pattern, in which components return Task and Task<TResult> objects instead of raising events through SynchronizationContext. Task-based APIs are the future of asynchronous programming in .NET.

##Examples of Library Support for SynchronizationContext

Simple components such as BackgroundWorker and WebClient are implicitly portable by themselves, hiding the SynchronizationContext capture and usage. Many libraries have a more visible use of SynchronizationContext. By exposing APIs using SynchronizationContext, libraries not only gain framework independence, they also provide an extensibility point for advanced end users.

In addition to the libraries I’ll discuss now, the current SynchronizationContext is considered to be part of the ExecutionContext. Any system that captures a thread’s ExecutionContext captures the current SynchronizationContext. When the ExecutionContext is restored, the SynchronizationContext is usually restored as well.

###Windows Communication Foundation (WCF):UseSynchronizationContext
WCF has two attributes that are used to configure server and client behavior: ServiceBehaviorAttribute and CallbackBehaviorAttribute. Both of these attributes have a Boolean property: UseSynchronizationContext. The default value of this attribute is true, which means that the current SynchronizationContext is captured when the communication channel is created, and this captured SynchronizationContext is used to queue the contract methods.

Normally, this behavior is exactly what is needed: Servers use the default SynchronizationContext, and client callbacks use the appropriate UI SynchronizationContext. However, this can cause problems when re-entrancy is desired, such as a client invoking a server method that invokes a client callback. In this and similar cases, the WCF automatic usage of SynchronizationContext may be disabled by setting UseSynchronizationContext to false.

This is just a brief description of how WCF uses SynchronizationContext. See the article “Synchronization Contexts in WCF” (<msdn.microsoft.com/magazine/cc163321>) in the November 2007 issue of MSDN Magazine for more details.

###Windows Workflow Foundation (WF): WorkflowInstance.SynchronizationContext
WF hosts originally used WorkflowSchedulerService and derived types to control how workflow activities were scheduled on threads. Part of the .NET Framework 4 upgrade included the SynchronizationContext property on the WorkflowInstance class and its derived WorkflowApplication class.

The SynchronizationContext may be set directly if the hosting process creates its own WorkflowInstance. SynchronizationContext is also used by WorkflowInvoker.InvokeAsync, which captures the current SynchronizationContext and passes it to its internal WorkflowApplication. This SynchronizationContext is then used to post the workflow completion event as well as the workflow activities.

###Task Parallel Library (TPL): TaskScheduler.FromCurrentSynchronizationContext and CancellationToken.Register
The TPL uses task objects as its units of work and executes them via a TaskScheduler. The default TaskScheduler acts like the default SynchronizationContext, queuing the tasks to the ThreadPool. There’s another TaskScheduler provided by the TPL queue that queues tasks to a SynchronizationContext. Progress reporting with UI updates may be done with a nested task, as shown in Figure 5.

####Figure 5 Progress Reporting with UI Updates
```C#
private void button1_Click(object sender, EventArgs e)
{
  // This TaskScheduler captures SynchronizationContext.Current.
  TaskScheduler taskScheduler = TaskScheduler.FromCurrentSynchronizationContext();
  // Start a new task (this uses the default TaskScheduler, 
  // so it will run on a ThreadPool thread).
  Task.Factory.StartNew(() =>
  {
    // We are running on a ThreadPool thread here.

  
    ; // Do some work.

  // Report progress to the UI.
    Task reportProgressTask = Task.Factory.StartNew(() =>
      {
        // We are running on the UI thread here.
        ; // Update the UI with our progress.
      },
      CancellationToken.None,
      TaskCreationOptions.None,
      taskScheduler);
    reportProgressTask.Wait();
  
    ; // Do more work.
  });
}
```

The CancellationToken class is used for any type of cancellation in the .NET Framework 4. To integrate with existing forms of cancellation, this class allows registering a delegate to invoke when cancellation is requested. When the delegate is registered, a SynchronizationContext may be passed. When the cancellation is requested, CancellationToken queues the delegate to the SynchronizationContext instead of executing it directly.

###Microsoft Reactive Extensions (Rx): ObserveOn, SubscribeOn and SynchronizationContextScheduler
Rx is a library that treats events as streams of data. The ObserveOn operator queues events through a SynchronizationContext, and the SubscribeOn operator queues the subscriptions to those events through a SynchronizationContext. ObserveOn is commonly used to update the UI with incoming events, and SubscribeOn is used to consume events from UI objects.

Rx also has its own way of queuing units of work: the IScheduler interface. Rx includes SynchronizationContextScheduler, an implementation of IScheduler that queues to a SynchronizationContext.

###Visual Studio Async CTP: await, ConfigureAwait, SwitchTo and EventProgress<T>
The Visual Studio support for asynchronous code transformations was announced at the Microsoft Professional Developers Conference 2010. By default, the current SynchronizationContext is captured at an await point, and this SynchronizationContext is used to resume after the await (more precisely, it captures the current SynchronizationContext unless it is null, in which case it captures the current TaskScheduler):

```C#
private async void button1_Click(object sender, EventArgs e)
{
  // SynchronizationContext.Current is implicitly captured by await.
  var data = await webClient.DownloadStringTaskAsync(uri);
  // At this point, the captured SynchronizationContext was used to resume
  // execution, so we can freely update UI objects.
}
```

ConfigureAwait provides a means to avoid the default SynchronizationContext capturing behavior; passing false for the flowContext parameter prevents the SynchronizationContext from being used to resume execution after the await. There’s also an extension method on SynchronizationContext instances called SwitchTo; this allows any async method to change to a different SynchronizationContext by invoking SwitchTo and awaiting the result.

The asynchronous CTP introduces a common pattern for reporting progress from asynchronous operations: the IProgress<T> interface and its implementation EventProgress<T>. This class captures the current SynchronizationContext when it’s constructed and raises its ProgressChanged event in that context.

In addition to this support, void-returning async methods will increment the asynchronous operation count at their start and decrement it at their end. This behavior makes void-returning async methods act like top-level asynchronous operations.

##Limitations and Guarantees

Understanding SynchronizationContext is helpful for any programmer. Existing cross-framework components use it to synchronize their events. Libraries may expose it to allow advanced flexibility. The savvy coder who understands the limitations and guarantees of SynchronizationContext is better able to write and consume such classes.

---------

Stephen Cleary has had an interest in multithreading ever since he first heard of the concept. He’s completed many business-critical multitasking systems for major clients including Syracuse News, R. R. Donnelley and BlueScope Steel. He regularly speaks at .NET user groups, BarCamps and Day of .NET events near his home in Northern Michigan, usually on a multithreading topic. He maintains a programming blog at nitoprograms.com.

Thanks to the following technical expert for reviewing this article: Eric Eilebrecht