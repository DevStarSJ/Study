class Program
{
    static bool IsArmstrongNumber(int n)
    {
        if (n < 100 || n > 999)
            return false;

        int n1 = n / 100;
        int n2 = n % 100 / 10;
        int n3 = n % 10;

        int r1 = n1 * n1 * n1;
        int r2 = n2 * n2 * n2;
        int r3 = n3 * n3 * n3;

        return n == r1 + r2 + r3;
    }
    static void Main(string[] args)
    {
        System.Console.WriteLine(string.Format("{0} is Armstrong Number ? {1}",
            379, IsArmstrongNumber(379) ? "True" : "False"));

        System.Console.WriteLine(string.Format("{0} is Armstrong Number ? {1}",
            371, IsArmstrongNumber(371) ? "True" : "False"));
    }
}

