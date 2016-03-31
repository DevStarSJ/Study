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
