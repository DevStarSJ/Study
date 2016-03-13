class Program

{
    public static int Fibonacci(int n)
    {
        if (0 <= n && n <= 2)
            return n;

        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }

static void Main(string[] args)
    {
        for (int i = 1; i <= 10; i++)
        {
            System.Console.WriteLine(string.Format("Fibonacci {0} : {1}", i, Fibonacci(i)));
        }
        System.Console.WriteLine(string.Format("Fibonacci 44th : {0}", Fibonacci(44)));
    }
}