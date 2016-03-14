##Fibonacci Sequence

Write a function to print nth number in Fibonacci series?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

피보나찌 수열 (황금비) 을 계산하세요.

---

일단 피보나찌 수열이 무엇인지는 Link를 참조해 주세요.

<https://en.wikipedia.org/wiki/Fibonacci_number>

`황금비` 라고 해서 사람의 눈에 가장 자연스러운 가로 세로 비율을 나타내는데 많이 사용됩니다.

가장 간단한 방법은 재귀함수(Recursive Function)을 이용하여 구현을 하면됩니다.

통상적으로 학교에서 배운 방법입니다.

하지만 이 방법으로 44번째 Fibonacci Number를 계산할 경우 이미 계산된 결과를 재사용하지 못해서 엄청나게 많은 Call Stack이 쌓입니다.  

이 문제를 해결하기 위해서는 뒤에서 부터 Recursive 하게 호출하는 방법을 사용하지 말고 앞에서부터 계산하면 해결됩니다.  

또다른 방법으로는 한 번 계산된 결과를 별도의 Array에 저장을 해서 재활용하는 방법을 이용하는 방법도 있습니다.


###C Sharp (basic implementation)

```C#
class Program
{
    public static int Fibonacci(int n)
    {
        if (0 <= n && n <= 2)
            return n;

        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }

static void Main(string[] args)
    {
        for (int i = 1; i <= 10; i++)
        {
            System.Console.WriteLine(string.Format("Fibonacci {0} : {1}", i, Fibonacci(i)));
        }
        System.Console.WriteLine(string.Format("Fibonacci 44th : {0}", Fibonacci(44)));
    }
}
```

###C Sharp (reusing calculation)
```C#
using System.Collections.Generic;
using System.Linq;

class Program
{
    static List<int> FibonacciSeries = new List<int>();

    public static int GetFibonacciNumber(int n)
    {
        int nCnt = FibonacciSeries.Count();
        if (n <= nCnt)
        {
            return FibonacciSeries[n - 1];
        }
        else
        {
            int ret = 0;
            if (n == 1)
            {
                FibonacciSeries.Add(1);
                ret = 1;
            }
            else if (n == 2)
            {
                if (FibonacciSeries.Count() == 0)
                {
                    FibonacciSeries.Add(1);
                }

                FibonacciSeries.Add(2);
                ret = 2;
            }
            else
            {
                ret = GetFibonacciNumber(n - 1) + GetFibonacciNumber(n - 2);
                FibonacciSeries.Add(ret);
            }

            return ret;
        }
    }

    static void Main(string[] args)
    {
        for (int i = 1; i <= 10; i++)
        {
            System.Console.WriteLine(string.Format("Fibonacci {0} : {1}", i, GetFibonacciNumber(i)));
        }
        System.Console.WriteLine(string.Format("Fibonacci 44 : {0}", GetFibonacciNumber(44)));
    }
}
```
