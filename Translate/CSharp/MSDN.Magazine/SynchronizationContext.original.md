EBRUARY 2011VOLUME 26 NUMBER 02

#Parallel Computing - It's All About the SynchronizationContext

By Stephen Cleary | February 2011

Multithreaded programming can be quite difficult, and there’s a tremendous body of concepts and tools to learn when one embarks on this task. To help out, the Microsoft .NET Framework provides the SynchronizationContext class. Unfortunately, many developers aren’t even aware of this useful tool.

Regardless of the platform—whether it’s ASP.NET, Windows Forms, Windows Presentation Foundation (WPF), Silverlight or others—all .NET programs include the concept of SynchronizationContext, and all multithreading programmers can benefit from understanding and applying it.

##The Need for SynchronizationContext

Multithreaded programs existed well before the advent of the .NET Framework. These programs often had the need for one thread to pass a unit of work to another thread. Windows programs were centered on message loops, so many programmers used this built-in queue to pass units of work around. Each multithreaded program that wanted to use the Windows message queue in this fashion had to define its own custom Windows message and convention for handling it.

When the .NET Framework was first released, this common pattern was standardized. At that time, the only GUI application type that .NET supported was Windows Forms. However, the framework designers anticipated other models, and they developed a generic solution. ISynchronizeInvoke was born.

The idea behind ISynchronizeInvoke is that a “source” thread can queue a delegate to a “target” thread, optionally waiting for that delegate to complete. ISynchronizeInvoke also provided a property to determine whether the current code was already running on the target thread; in this case, queuing up the delegate would be unnecessary. Windows Forms provided the only implementation of ISynchronizeInvoke, and a pattern was developed for designing asynchronous components, so everyone was happy.

Version 2.0 of the .NET Framework contained many sweeping changes. One of the major improvements was introducing asynchronous pages to the ASP.NET architecture. Prior to the .NET Framework 2.0, every ASP.NET request needed a thread until the request was completed. This was an inefficient use of threads, because creating a Web page often depends on database queries and calls to Web services, and the thread handling that request would have to wait until each of those operations finished. With asynchronous pages, the thread handling the request could begin each of the operations and then return back to the ASP.NET thread pool; when the operations finished, another thread from the ASP.NET thread pool would complete the request.

However, ISynchronizeInvoke wasn’t a good fit for the ASP.NET asynchronous pages architecture. Asynchronous components developed using the ISynchronizeInvoke pattern wouldn’t work correctly within ASP.NET pages because ASP.NET asynchronous pages aren’t associated with a single thread. Instead of queuing work to the original thread, asynchronous pages only need to maintain a count of outstanding operations to determine when the page request can be completed. After much thought and careful design, ISynchronizeInvoke was replaced by SynchronizationContext.

##The Concept of SynchronizationContext

ISynchronizeInvoke satisfied two needs: determining if synchronization was necessary, and queuing a unit of work from one thread to another. SynchronizationContext was designed to replace ISynchronizeInvoke, but after the design process, it turned out to not be an exact replacement.

One aspect of SynchronizationContext is that it provides a way to queue a unit of work to a context. Note that this unit of work is queued to a context rather than a specific thread. This distinction is important, because many implementations of SynchronizationContext aren’t based on a single, specific thread. SynchronizationContext does not include a mechanism to determine if synchronization is necessary, because this isn’t always possible.

Another aspect of SynchronizationContext is that every thread has a “current” context. A thread’s context isn’t necessarily unique; its context instance may be shared with other threads. It’s possible for a thread to change its current context, but this is quite rare.

A third aspect of SynchronizationContext is that it keeps a count of outstanding asynchronous operations. This enables the use of ASP.NET asynchronous pages and any other host needing this kind of count. In most cases, the count is incremented when the current SynchronizationContext is captured, and the count is decremented when the captured SynchronizationContext is used to queue a completion notification to the context.

There are other aspects of SynchronizationContext, but they’re less important to most programmers. The most important aspects are illustrated in Figure 1.

####Figure 1 Aspects of the SynchronizationContext API
```C#
// The important aspects of the SynchronizationContext APIclass SynchronizationContext 
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

##The Implementations of SynchronizationContext

The actual “context” of the SynchronizationContext isn’t clearly defined. Different frameworks and hosts are free to define their own context. Understanding these different implementations and their limitations clarifies exactly what the SynchronizationContext concept does and doesn’t guarantee. I’ll briefly discuss some of these implementations.

###WindowsFormsSynchronizationContext
(System.Windows.Forms.dll: System.Windows.Forms) Windows Forms apps will create and install a WindowsFormsSynchronizationContext as the current context for any thread that creates UI controls. This SynchronizationContext uses the ISynchronizeInvoke methods on a UI control, which passes the delegates to the underlying Win32 message loop. The context for WindowsFormsSynchronizationContext is a single UI thread.

All delegates queued to the WindowsFormsSynchronizationContext are executed one at a time; they’re executed by a specific UI thread in the order they were queued. The current implementation creates one WindowsFormsSynchronizationContext for each UI thread.

###DispatcherSynchronizationContext
(WindowsBase.dll: System.Windows.Threading) WPF and Silverlight applications use a DispatcherSynchronizationContext, which queues delegates to the UI thread’s Dispatcher with “Normal” priority. This SynchronizationContext is installed as the current context when a thread begins its Dispatcher loop by calling Dispatcher.Run. The context for DispatcherSynchronizationContext is a single UI thread.

All delegates queued to the DispatcherSynchronizationContext are executed one at a time by a specific UI thread in the order they were queued. The current implementation creates one DispatcherSynchronizationContext for each top-level window, even if they all share the same underlying Dispatcher.

###Default (ThreadPool) SynchronizationContext
(mscorlib.dll: System.Threading) The default SynchronizationContext is a default-constructed SynchronizationContext object. By convention, if a thread’s current SynchronizationContext is null, then it implicitly has a default SynchronizationContext.

The default SynchronizationContext queues its asynchronous delegates to the ThreadPool but executes its synchronous delegates directly on the calling thread. Therefore, its context covers all ThreadPool threads as well as any thread that calls Send. The context “borrows” threads that call Send, bringing them into its context until the delegate completes. In this sense, the default context may include any thread in the process.

The default SynchronizationContext is applied to ThreadPool threads unless the code is hosted by ASP.NET. The default SynchronizationContext is also implicitly applied to explicit child threads (instances of the Thread class) unless the child thread sets its own SynchronizationContext. Thus, UI applications usually have two synchronization contexts: the UI SynchronizationContext covering the UI thread, and the default SynchronizationContext covering the ThreadPool threads.

Many event-based asynchronous components don’t work as expected with the default SynchronizationContext. An infamous example is a UI application where one BackgroundWorker starts another BackgroundWorker. Each BackgroundWorker captures and uses the SynchronizationContext of the thread that calls RunWorkerAsync and later executes its RunWorkerCompleted event in that context. In the case of a single BackgroundWorker, this is usually a UI-based SynchronizationContext, so RunWorkerCompleted is executed in the UI context captured by RunWorkerAsync (see Figure 2).

<image: A Single BackgroundWorker in a UI Context>
--그림1--

####Figure 2 A Single BackgroundWorker in a UI Context

However, if the BackgroundWorker starts another BackgroundWorker from its DoWork handler, then the nested BackgroundWorker doesn’t capture the UI SynchronizationContext. DoWork is executed by a ThreadPool thread with the default SynchronizationContext. In this case, the nested RunWorkerAsync will capture the default SynchronizationContext, so it will execute its RunWorkerCompleted on a ThreadPool thread instead of a UI thread (see Figure 3).

<image: Nested BackgroundWorkers in a UI Context>
--그림2--

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

 	Specific Thread Used to Execute Delegates	Exclusive (Delegates Execute One at a Time)	Ordered (Delegates Execute in Queue Order)	Send May Invoke Delegate Directly	Post May Invoke Delegate Directly
Windows Forms	Yes	Yes	Yes	If called from UI thread	Never
WPF/Silverlight	Yes	Yes	Yes	If called from UI thread	Never
Default	No	No	No	Always	Never
ASP.NET	No	Yes	No	Always	Always

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