### 9.2 Interrupting threads

- long-running thread를 정지시키는데는 singnal로 처리하는 것이 좋습니다.
  - thread pool에 의해 동작중인 thread가 있는 상태에서 thread pool을 해제해야 할 경우
  - thread 동작을 사용자가 명시적으로 취소할 경우
  - 기타 다른 상황들에서 이런 작업이 필요한 경우가 있습니다.

- 어떤 상황이든 그 처리 방법은 같습니다.
  - thread의 처리가 원래대로 종료시점까지 실행되기 전에 signal을 보내서, 더 이상 실행되지 않고 빠져나오게 해야 합니다.

- 각각의 경우별로 구현을 해도 되지만, 우리 그러지 맙시다. 예 ?
  - thread 관련 구현은 의도대로 잘 되지 않을 경우가 많아서 제대로 돌아가는지 확인을 해야 합니다.
  - 하지만, 일반적인 메커니즘으로 구현하면, 한번만 검증을 제대로 마친 뒤 계속해서 믿고 쓸 수 있습니다.

- C++11에서 interrupting thread와 관련된 기능을 제공해주지는 않습니다.
  - 하지만 어렵지 않게 구현할 수 있습니다.
  - interrupting thread를 보기전에 먼저 thread의 시작 및 interrupt에 대한 interface 부터 살펴보기로 하겠습니다.

#### 9.2.1 Launching and interrupting another thread

- 우선 external interface부터 생각해 보겠습니다.
  - thread가 interrupt 가능하게 하기 위해서는 뭐가 필요할까요 ?
  - 당연히 std::thread 에 interrupt() 함수를 추가해야 합니다.

```C++
class interruptible_thread
{
public:
    template<typename FunctionType>
    interrputible_thread(FunctionType f);
    void join();
    void detach();
    bool joinable() const;
    void interrput();
};
```

- 기본적으로 std::thread를 이용하고, interruption handling에 일부만 구현하면 됩니다.
- thread 입장에서 뭐가 필요할까요 ?
  - `나(thread)는 여기서 interrupt 처리를 해도 된다.` 는 바로 그 interruption point가 중요합니다.
  - 다른 추가 정보 없이 (parameter 없이) 동작하는 함수 `interruption_point()` 을 추가해 보도록 하겠습니다.
  - thread의 상태를 저장하는 local 변수를 선언하여서 thread가 시작될 때 set 한 다음에 interruption_point() 함수에서 그 값을 제어하도록 구현 하면 됩니다.
- thread_local flag가 필요하기 때문에 일반적인 std::thread를 그대로 사용할 수 없습니다.
  - interruptible_thread를 제어하기 위해서는 이 변수가 필수적입니다.
  - std::thread가 시작되기전에 이 기능이 수행되도록 constuctor로 감싸야 합니다.

```C++
class interrupt_flag
{
public:
    void set();
    bool is_set() const;
};

thread_local interrupt_flag this_thread_interrupt_flag; // #1

class interruptible_thread
{
    std::thread internal_thread;
    interrupt_flag* flag;
public:
    template<typename FunctionType>
    interruptible_thread(FunctionType f)
    {
        std::promise<interrupt_flag*> p;               // #2
        internal_thread = std::thread([f, &p] {        // #3
                p.set_value(&this_thread_interrupt_flag);
                f();                                   // #4
            });
        flag = p.get_future().get();                   // #5
    }
    void interrupt()
    {
        if (flag)
        {
            flag->set();                               //#6
        }
    }
};
```

- 실제로 작업을 수행할 f 함수와 local promise 객체 p (#2) 를 감싼 lambda 식이 있습니다. (#3)
  - lambda식 안에서 promise의 값을 thread_local로 선언된 `this_thread_interrupt_flag` (#1)의 주소로 설정합니다.
  - 그렇게 set 한 다음에 새로운 thread를 할당하여 공급된 함수의 copy(사본)을 수행합니다. (#4)
- thread를 수행한 다음에 future와 연관된 promise가 준비되어서 그 결과를 flag라는 멤버변수에 줄때까지 기다립니다. (#5)
- lambda가 new thread를 수행중이고, 지역변수 p가 dangling reference라도 별 문제는 없습니다.
  - 왜냐하면 interruptible_thread의 생성자는 p가 더이상 실행하기 전의 new thread가 더이상 참조되지 않을때까지 기다립니다.
  - 이 구현은 thread의 join , detach 여부에 대해서 고려하지 않습니다.
  - thread가 종료되거나 detach 되었을 때 flag가 clear 되었는지만 확인하여 dangling pointer를 방지하면 됩니다.
- interrupt() 함수는 간단합니다.
  - interrupt flag에 대한 pointer를 가지고 있는 경우, interrupt 시킬 thread에 대해서 flag를 set하면 됩니다. (#6)

#### 9.2.2 Detecting that a thread has been interrupted

- 이제 interruption flag를 설정할 수 있게 되었습니다.
  - 다음으로는 thread가 실제로 중단되었는지 여부를 확인해 보도록 하겠습니다.
  - 가장 간단한 방법의 interruption_point() 함수를 사용하도록 하겠습니다.
    - thread 내의 interrupt되어도 안전한 곳에서 이 함수를 호출합니다.
    - flag가 설정된 경우라면 thread_interrupted 예외를 throw 하면 됩니다.

```C++
void interruption_point()
{
    if (this_thread_interrupt_flag.is_set())
        throw thread_interrupted();
}
```

사용은 이렇게 하면 됩니다.

```C++
void F()
{
    while(!done)
    {
        interruption_point();
        process_next_item();
    }
}
```

- 이것은 동작하는 code이긴 하지만, 이상적인 방법은 아닙니다.
  - thread를 interrupt하기 위한 최고의 장소중 하나는 thread가 interrupt_point()를 호출하기 위해 실행되고 있지 않는 것을 기다리면서 block된 상태이다.
  - interrupt 방식에 따라 뭔가를 기다리는 수단이 필요합니다. (?)

#####Listing 9.10 std::condition_variable 을 사용한 interruptible_wait (broken version)

```C++
void interruptible_wait(std::condition_variable& cv, std::uniduq_lock<std::mux>& lk)
{
    interruption_point();
    this_thread_interrupt_flag.set_condition_variable(cv);  // #1
    cv.wait(lk);                                            // #2
    this_thread_interrupt_falg.clear_condition_variable();  // #3
    interruption_point();
}
```

- interrupt flag 와 condition variable의 관계를 설정하고 해제하는 좋고 간단한 code 입니다.
  1. interrupt를 check.
  1. thread의 interrupt_flag와 condition_variable을 연결. #1
  1. condition_variable을 wait #2
  1. condition_variable의 연결 해제 #3
  1. interrupt를 다시 한번 check.
- condition_variable을 wait하는 동안 interrupt가 발생한 경우라면,
  - 해당 thread는 condition_variable을 통해서, wait 상태를 깨울 것입니다.
  - 그래서, interrupt의 확인이 가능합니다.
- 불행하게도, 이 code는 못씁니다. 2가지 문제가 있습니다.
  1. `std::condition_variable::wait()`에서 예외발생시 interrupt_flag와의 관계를 해제하지 않고 빠져나오게 됩니다.
    - destructor와 연결되는 구조를 활용하면 쉽게 고칠 수 있습니다.
  1. `race condition`(경쟁 조건)이 있습니다.
    - interrupt_point()와 wait() 사이에 있을 때 interrupt가 발생한 경우,
      - condition_variable는 interrupt_flag와의 관계에 대해서는 신경쓰지 않습니다.
        - 왜냐하면, thread는 wait 상태가 아니기 때문에 condition_variable을 notify 할 수 없습니다.
    - interrupt_point()와 wait() 사이에서의 interrupt에 대한 notify 방안을 생각해야 합니다.
      - std::condition_variable의 내부 구현을 살펴보지 않고도 이 문제를 해결하는 방법은 딱 한가지밖에 없습니다.
        - set_condition_variable() 호출을 보호하는 용도의 mutex를 사용하는 것입니다.
    - 그런데, 이러면 또다른 문제가 발생합니다.
      - thread #2를 lock 시킬 다른 thread #1의 수명도 모른체 mutex의 참조를 통과시켜야 합니다. 
        - thread #1 : interrupt()를 호출하는 thread
        - thread #2 : interrupt 될 thread
      - thread #2가 이미 mutex를 lock 한지 그 여부도 모른체 위 작업을 해야 합니다.

- This has the potential for deadlock and the potential to access a mutex after it has already been destroyed, so it’s a nonstarter. 부터 할 차례
