##Check Prime Number

Algorithm to check if a number is Prime or not?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

소수인지 검사하세요.

---

소수(Prime Number)란 ? 자기자신과 1로만 나누어 떨어지는 수를 의미합니다.

###C Sharp

```C#
class Program
{
    static bool IsPrimeNumber(int num)
    {
        if (num == 1 || num == 2)
            return true;

        for (int i = 2; i < num; i++)
        {
            if (num % i == 0)
                return false;
        }
        return true;
    }
    static void Main(string[] args)
    {
        System.Console.WriteLine(string.Format(
            "{0} is Prime Number ? {1}", 27, IsPrimeNumber(27) ? "Yes" : "No"));

        System.Console.WriteLine(string.Format(
            "{0} is Prime Number ? {1}", 37, IsPrimeNumber(37) ? "Yes" : "No"));
    }
}
```
