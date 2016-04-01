##Selection Sort

Sorting an Array using Selection Sort

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

Selection Sort(선택정렬)을 구현하세요.

Selection Sort가 무엇인지는 아래 Link를 참조하세요.

<https://en.wikipedia.org/wiki/Selection_sort>

---

###C# 
```C#
using System;

class Program
{
    static void SelectionSort<T>(ref T[] array ) where T : IComparable
    {
        for (int i = 0; i < array.Length; i++)
        {
            T minValue = array[i];
            int minIndex = i;

            for (int j = i + 1; j < array.Length; j++)
            {
                if (array[j].CompareTo(minValue) < 0)
                {
                    minValue = array[j];
                    minIndex = j;
                }
            }

            if (i != minIndex)
            {
                T temp = array[i];
                array[i] = minValue;
                array[minIndex] = temp;
            }
        }
    }
    static void Main(string[] args)
    {
        int[] array = { 9, 4, 6, 5, 7, 8, 3, 2, 1, 0 };

        SelectionSort<int>(ref array);

        foreach(int n in array)
        {
            Console.Write($"{n}\t");
        }

        Console.WriteLine();
    }
}
```
