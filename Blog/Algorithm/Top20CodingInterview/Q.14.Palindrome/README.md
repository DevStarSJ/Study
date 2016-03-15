##Check Palindrome

Algorithm to check if a number is Palindrome?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

Palindrome인지 검사하세요.

---

Palindrome란 ? 문자, 숫자의 순서가 앞에서 읽은 것과 뒤에서 읽은 것이 같은 것을 의미합니다.

가장 대표적인 예제로는 다음과 같은 것들이 있습니다.

>"A man, a plan, a canal, Panama!", "Amor, Roma", "race car", "stack cats", "step on no pets", "taco cat", "put it up", "Was it a car or a cat I saw?" and "No 'x' in Nixon".

<https://en.wikipedia.org/wiki/Palindrome>

###C Sharp

```C#
class Program
{
    static bool IsCharOrNumber(char c)
    {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '1' && c <= '0');
    }

    static bool IsPalindrome(string str)
    {
        str = str.ToLower();

        int forward = 0;
        int backward = str.Length - 1;

        while (forward < backward)
        {
            while (!IsCharOrNumber(str[forward]))
                forward++;

            while (!IsCharOrNumber(str[backward]))
                backward--;

            if (str[forward] != str[backward])
                return false;

            forward++;
            backward--;
        }

        return true;
    }

    static void Main(string[] args)
    {
        System.Console.WriteLine(string.Format("[{0}] is Palindrome ? {1}",
            "A man, a plan, a canal, Panama!",
            IsPalindrome("A man, a plan, a canal, Panama!") ? "Yes" : "No"));

        System.Console.WriteLine(string.Format("[{0}] is Palindrome ? {1}",
            "LunaStar the Silver",
            IsPalindrome("LunaStar the Silver") ? "Yes" : "No"));
    }
}
```
