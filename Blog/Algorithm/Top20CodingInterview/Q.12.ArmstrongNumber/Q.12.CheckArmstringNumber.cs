class Program
{
    static bool IsArmstrongNumber(int num)
    {
        int step = num;
        int sum = 0;

        while (step != 0)
        {
            int digit = step % 10;
            sum += digit * digit * digit;
            step /= 10;
        }

        return num == sum;
    }
    static void Main(string[] args)
    {
        System.Console.WriteLine(string.Format("{0} is Armstrong Number ? {1}",
            379, IsArmstrongNumber(379) ? "True" : "False"));

        System.Console.WriteLine(string.Format("{0} is Armstrong Number ? {1}",
            371, IsArmstrongNumber(371) ? "True" : "False"));
    }
}

