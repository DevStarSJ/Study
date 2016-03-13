using System.Collections.Generic;
using System.Linq;

class Program

{
    static List<int> FibonacciSeries = new List<int>();

    public static int GetFibonacciNumber(int n)
    {
        int nCnt = FibonacciSeries.Count();
        if (n <= nCnt)
        {
            return FibonacciSeries[n - 1];
        }
        else
        {
            int ret = 0;
            if (n == 1)
            {
                FibonacciSeries.Add(1);
                ret = 1;
            }
            else if (n == 2)
            {
                if (FibonacciSeries.Count() == 0)
                {
                    FibonacciSeries.Add(1);
                }

                FibonacciSeries.Add(2);
                ret = 2;
            }
            else
            {
                ret = GetFibonacciNumber(n - 1) + GetFibonacciNumber(n - 2);
                FibonacciSeries.Add(ret);
            }

            return ret;
        }
    }

    static void Main(string[] args)
    {
        for (int i = 1; i <= 10; i++)
        {
            System.Console.WriteLine(string.Format("Fibonacci {0} : {1}", i, GetFibonacciNumber(i)));
        }
        System.Console.WriteLine(string.Format("Fibonacci 44 : {0}", GetFibonacciNumber(44)));
    }
}
