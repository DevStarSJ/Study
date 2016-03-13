##Check Anagram

Write a Program which checks if two Strings are Anagram or not?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

두 단어가 Anagram인지 체크하세요.

- Anagram : 원본 단어의 철자의 순서를 재배열하여 만든 단어

<https://en.wikipedia.org/wiki/Anagram>

###C Sharp

```C#
using System.Collections.Generic;

class Program
{
    static bool IsAnagram(string str1, string str2)
    {
        if (str1.Length != str2.Length)
            return false;
        
        string s1 = str1.ToLower();
        string s2 = str2.ToLower();

        Dictionary<char, int> dic = new Dictionary<char, int>();

        foreach(char c in s1)
        {
            if (dic.ContainsKey(c))
                dic[c] += 1;
            else
                dic.Add(c, 1);
        }

        foreach (char c in s2)
        {
            if (dic.ContainsKey(c))
            {
                dic[c] -= 1;
                if (dic[c] < 0)
                    return false;
            }
            else
                return false;
        }
        return true;
    }

    static void Main(string[] args)
    {
        System.Console.WriteLine(IsAnagram("Duty", "TYDU"));
        System.Console.WriteLine(IsAnagram("LunaStar", "Demilune"));
    }
}
```
