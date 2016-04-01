class Program
{
    static int SumDigits(int number)
    {
        if (number < 0)
            number *= -1;

        if (number < 10)
            return number;

        return number % 10 + SumDigits(number / 10);
    }
    static void Main(string[] args)
    {
        int[] digits = { 123456, 654321, -126543 };
        int[] result = { SumDigits(digits[0]),
                         SumDigits(digits[1]),
                         SumDigits(digits[2]) };

        for (int i = 0; i < result.Length; i++)
        {
            System.Console.WriteLine($"Sum Digits of {digits[i]} is {result[i]}");
        }
    }
}
