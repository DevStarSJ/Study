##Find Pair Sum of Equal

How to find all pairs of elements in an integer array, whose sum is equal to a given number?  

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

숫자 배열에서 주어진 값과 합이 같은 쌍(pair)을 모두 찾으세요.

---

기본적인 for문을 사용할 수 있는지를 묻는 문제로 판단됩니다.

###C Sharp

```C#
using System.Collections.Generic;
using System.Linq;

class Program
{
    static List<KeyValuePair<int, int>> FindPairSumOfEqual(List<int> list, int sum)
    {
        List<KeyValuePair<int, int>> answer = new List<KeyValuePair<int, int>>();

        int nCnt = list.Count();

        for (int i = 0; i < nCnt; i++)
        {
            for (int j = i+1; j < nCnt; j++)
            {
                if (list[i] + list[j] == sum)
                    answer.Add(new KeyValuePair<int, int>(list[i], list[j]));
            }
        }

        return answer;
    }
    static void Main(string[] args)
    {
        List<int> list = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        List<KeyValuePair<int, int>> ans10 = FindPairSumOfEqual(list, 10);

        foreach(KeyValuePair<int,int> pair in ans10)
        {
            System.Console.Write(string.Format("({0} , {1}) ", pair.Key, pair.Value));
        }
        System.Console.WriteLine();

        List<KeyValuePair<int, int>> ans15 = FindPairSumOfEqual(list, 15);

        foreach (KeyValuePair<int, int> pair in ans15)
        {
            System.Console.Write(string.Format("({0} , {1}) ", pair.Key, pair.Value));
        }
        System.Console.WriteLine();
    }
}
```
