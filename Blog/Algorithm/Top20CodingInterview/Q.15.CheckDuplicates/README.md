##Check Duplicates

Algorithm to find if Array contains duplicates? 

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

배열에 중복된 값이 있는지 검사하세요.

---

###C# 

```C#
using System;
using System.Collections.Generic;

class Program
{
    static bool HaveDuplicates<T>(List<T> list) where T : IComparable
    {
        int nCnt = list.Count;

        for (int i = 0; i < nCnt; i++)
        {
            for (int j = i + 1; j < nCnt; j++)
            {
                if (list[i].CompareTo(list[j]) == 0)
                    return true;
            }
        }

        return false;
    }
    static void Main(string[] args)
    {
        List<string> listStr = new List<string> { "Luna", "Star", "Silver", "Dev", "star", "luna" };
        List<int> listInt = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 5 };

        Console.WriteLine(string.Format("{0} have duplicates ? {1}",
            nameof(listStr), HaveDuplicates<string>(listStr) ? "Yes" : "No"));

        Console.WriteLine(string.Format("{0} have duplicates ? {1}",
            nameof(listInt), HaveDuplicates<int>(listInt) ? "Yes" : "No"));
    }
}
```
