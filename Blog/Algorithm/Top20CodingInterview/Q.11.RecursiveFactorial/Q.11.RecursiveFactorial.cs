class Program
{
    static int Factorial(int n)
    {
        return n == 1 ? 1 : n * Factorial(n - 1);
    }
    static void Main(string[] args)
    {
        System.Console.WriteLine(string.Format("{0} Factorial = {1}", 10, Factorial(10)));
    }
}
