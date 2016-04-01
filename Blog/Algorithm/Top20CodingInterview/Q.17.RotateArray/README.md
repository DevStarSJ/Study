##Rotate Array

How to rotate an array by a given pivot ?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

Array를 주어진 Pivot(중심점) 만큼 Rotate하세요.

한마디로 Shift하되 밀려나간만큼 뒤에 다시 붙이라는 말입니다.

원문의 Link를 보면 기가 막힌 방법으로 단 하나의 임시변수만 할당하면서도 숫자들을 많이 이동시키지 않고 풀었더군요.  
대신 그것을 보고 실제로 맞게 동작하는지를 해석하는데 시간이 좀 걸렸습니다.  

저는 그냥 array크기만큼의 임시공간을 사용했지만,  
그냥 누가봐도 이해하기 쉽게 작성하였습니다.  

---

###C# 
```C#
using System;

class Program
{
    static void Rotate(ref int[] array, int pivot)
    {
        if (pivot > array.Length)
            throw new ArgumentOutOfRangeException();

        int[] original = (int[])array.Clone();

        int nRotateCount = array.Length - pivot;

        for (int i = 0; i < nRotateCount; i++)
        {
            array[i] = original[i + pivot];
        }

        for (int i = nRotateCount; i < array.Length; i++)
        {
            array[i] = original[nRotateCount - i];
        }
    }
    static void Main(string[] args)
    {
        int[] array = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };

        Rotate(ref array, 1);

        foreach (int element in array)
        {
            Console.Write(string.Format("{0,4}", element));
        }

        Console.WriteLine("");
        Console.ReadKey();
    }
}
```
