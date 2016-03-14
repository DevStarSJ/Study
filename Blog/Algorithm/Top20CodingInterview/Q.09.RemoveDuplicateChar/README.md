##Remove Duplicate Characters

Write a function to remove duplicate characters from String ?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

문자열을 입력받아서 중복된 문자를 제거하세요.

---

대부분 언어의 string 타입에는 특정 문자 또는 문자열의 subset의 위치를 찾는 함수가 존재합니다.  

그것을 이용하여 해당 문자가 있는지 없는지 체크를 하면 쉽게 해결 할 수 있습니다.

###C Sharp

```C#
class Program
{
    static string RemoveDiplicateChar(string str)
    {
        string result = string.Empty;

        foreach(char c in str)
        {
            if (result.IndexOf(c) != -1)
                continue;
            result += c;
        }

        return result;
    }
    static void Main(string[] args)
    {
        string str1 = "I love you";
        System.Console.WriteLine(string.Format("{0} : {1}", str1, RemoveDiplicateChar(str1)));
    }
}
```
