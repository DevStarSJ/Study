class Program

{
    public static int Fibonacci(int n)
    {
        if (0 <= n && n <= 2)
            return n;

        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }

    public static int Fibonacci2(int n)
    {
        if (n < 3)
            return n;

        int nFirst = 1;
        int nSecond = 2;

        int nResult = 0;

        for (int i = 3; i <= n; i++)
        {
            nResult = nFirst + nSecond;
            nFirst = nSecond;
            nSecond = nResult;
        }
        return nResult;
    }

static void Main(string[] args)
    {
        for (int i = 1; i <= 10; i++)
        {
            System.Console.WriteLine(string.Format("Fibonacci {0} : {1}", i, Fibonacci2(i)));
        }
        System.Console.WriteLine(string.Format("Fibonacci 44th : {0}", Fibonacci2(44)));
    }
}