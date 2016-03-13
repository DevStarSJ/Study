class Program
{
    static void Main(string[] args)
    {
        int a = 30593;
        int b = 13953093;

        a ^= b;
        b ^= a;
        a ^= b;

        System.Console.WriteLine(a);
        System.Console.WriteLine(b);
    }
}