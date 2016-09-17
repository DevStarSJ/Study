## 2. thread 관리  

- 이번에 다룰 내용  
  + thread를 실행시키는 여러 가지 방법
  + thread가 끝나기를 기다리는 것과 실행되도록 내버려 두는 것의 비교
  + thread의 식별자 구분  

C++ Standard Library를 사용하면 std::thread 객체의 기능만으로도 thread 처리에 필요한 기능 대부분을 사용할 수 있습니다.  

### 2.1 기본적인 thread 관리  

모든 C++ 프로그램은 최소 1개의 thread ( `main()` )를 생성합니다.  
그런 다음 다른 함수를 실행시키는 thread를 실행 할 수 있습니다.  
main() 이 return 하면 프로그램이 종료하게 되듯이, thread로 실행한 함수가 return 하면 thread가 종료됩니다.  
특정 thread가 종료될 때까지 기다리는 것도 가능합니다. (ch.01의 예제에서 이미 해당 code가 소개되었습니다.)  

#### 2.1.1 thread 실행  

- thread는 std::thread 객체를 생성하면서 실행됩니다.
- 가장 간단한 형태는 parameter가 없고 return 값이 없는 function을 실행하는 것입니다.

```C++
#include <thread>

void F();
std::thread T(F);
```

- function 뿐만 아니라 callable type 의 객체도 std::thread의 생성자에 전달이 가능합니다.

```C++
class background_task
{
public:
    void operator()() const { do_something(); }
};

background_task B;
std::thread T(B);
```

- std::thread에 의해 실행되어지는 function object는 thread 실행시 그 영역으로 copy 되어져서 그 사본이 실행되는 것입니다.
- function object를 std::thread의 인자로 전달할 때 `C++ most vexing parse`가 일어나지 않도록 주의해야 합니다.
  - C++ most vexing parse 에 대한 자세한 사항은 아래 Link의 Post를 참고하세요.
    - [C++의 most vexing parse 를 조심하자.](http://devluna.blogspot.kr/2015/01/item-6-c-most-vexing-parse.html)
- 이름이 있는 variable을 전달하는게 아니라 type형을 그대로 전달할 경우 C++ most vexing parse가 발생 합니다.

```C++
std::thread T(background_task());
```

- 위 code는 background_task의 생성자를 통해 만들어진 객체가 전달되는게 아니라, background_task를 return 하고 인자가 없는 function pointer라고 인식합니다.
- 이 경우 괄호를 추가하거나 uniform initialization을 사용하면 C++ most vexing parse를 피할 수 있습니다.

```C++
std::thread T((background_task()));  // #1
std::thread T{ background_task() };  // #2
```

- `#1`의 경우 괄호를 추가하여 함수 선언으로 해석되는 것을 막았으며,
- `#2`의 경우에는 uniform initialization 문법을 사용하여 변수선언으로 인식하게 하였습니다.

- 이런 문제를 피하는 또 다른 방법은 lambda식을 사용하는 것입니다.
- 위의 예제를 lambda식을 활용하여 아래와 같이 표현 할 수 있습니다.

```C++
std::thread T([](){ do_something(); });
```

- thread를 시작한 뒤에는 그것이 끝나기를 기다릴 것인지 (`.join()`) 아니면 알아서 수행되도록 내버려 둘 것인지 (`.detach()`)를 선택 할 수 있습니다.
- std::thread 객체가 종료되기 전에 그 결정을 하지 않은 상태에서 프로그램이 종료되면 std::thread의 destructor는 std::terminate()를 호출합니다.
- std::thread 객체를 `.detach()`할 경우 thread는 std::object가 해제된 후에도 계속해서 동작하게 됩니다.
- 수행시킨 thread가 제대로 join 이나 detach 되었는지, 아니면 exception이 발생하였는지 확인하는건 필수적입니다.

- thread가 종료되길 기다리지 않기로 했다면, thread에서 사용하는 data 들이 thread 종료시까지 유효한지 확인을 해야 합니다.
  - thread에서 다른 function 내의 지역변수의 pointer 나 reference를 사용하는 경우에 thread 보다 먼저 해당 function이 종료된 경우에는 dangling pointer/reference를 가리키게 됩니다.

```C++
struct func
{
    int &i;
    func(int& i+) : i(i_) {}
    void operator() ()
    {
        for (unsigned j = 0; j < 1000000; ++j)
        {
            do_something(i);   // 1. Potential access to dangling reference
        }
    }
};

void oops()
{
    int localValue = 0;
    func F(localValue);
    std::thread T(F);
    T.detach();               // 2. Don't wait for thread to finish
}                             // 3. oops() is completed, but T might still be running
```

- 이 경우 oops()가 std::thread T 의 종료를 기다리지 않기로 결정했습니다.
- 그런데 T가 수행한 F에서 oops()의 지역변수 localValue를 이용하여 작업을 하고 있습니다.
- oops()가 종료된 후 해당 값들이 해제된 후에도 그 값들을 계속 사용하므로 올바르지 않은 결과가 나올 수 있습니다.
- 이런 문제는 thread 사용시의 문제가 아니라 single thread code에서도 피해야 하는 유형입니다.

- (p.17) 계속
