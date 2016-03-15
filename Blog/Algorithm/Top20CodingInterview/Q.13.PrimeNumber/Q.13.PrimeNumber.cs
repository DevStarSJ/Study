using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


class Program
{
    static bool IsPrimeNumber(int num)
    {
        if (num == 1 || num == 2)
            return true;

        for (int i = 2; i < num; i++)
        {
            if (num % i == 0)
                return false;
        }
        return true;
    }
    static void Main(string[] args)
    {
        System.Console.WriteLine(string.Format(
            "{0} is Prime Number ? {1}", 27, IsPrimeNumber(27) ? "Yes" : "No"));

        System.Console.WriteLine(string.Format(
            "{0} is Prime Number ? {1}", 37, IsPrimeNumber(37) ? "Yes" : "No"));
    }
}
