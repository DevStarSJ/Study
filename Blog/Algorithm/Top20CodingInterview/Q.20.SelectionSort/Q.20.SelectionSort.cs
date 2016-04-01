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
