##Calulate Factorial using Recursion

How to calculate factorial using recursion ?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

재귀함수를 이용하여 팩토리얼을 계산하세요.

---

###C Sharp

```C#
class Program
{
    static int Factorial(int n)
    {
        return n == 1 ? 1 : n * Factorial(n - 1);
    }
    static void Main(string[] args)
    {
        System.Console.WriteLine(string.Format("{0} Factorial = {1}", 10, Factorial(10)));
    }
}

```
