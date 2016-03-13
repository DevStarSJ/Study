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
