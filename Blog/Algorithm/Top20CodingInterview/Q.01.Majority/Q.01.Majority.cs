using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    private static int FindMajority(List<int> vNumbers)
    {
        int nMajority = vNumbers.Count() / 2;

        Dictionary<int, int> mExsitingNumber = new Dictionary<int, int>();

        foreach(int number in vNumbers)
        {
            if (mExsitingNumber.ContainsKey(number))
            {
                mExsitingNumber[number] += 1;
                if (mExsitingNumber[number] >= nMajority)
                {
                    return number;
                }
            }
            else
            {
                mExsitingNumber.Add(number, 1);
            }
        }

        throw new Exception("There is no Majority");
    }

    static void Main(string[] args)
    {
        List<int> vNumbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        try
        {
            int nMajority = FindMajority(vNumbers);

            System.Console.WriteLine(nRet);
        }
        catch (Exception e)
        {
            System.Console.WriteLine(e.Message);
        }

        try
        {
            System.Console.WriteLine(
                FindMajority(
                    new List<int> { 1, 2, 3, 3, 3, 3, 4, 5, 3 }));
        }
        catch (Exception e)
        {
            System.Console.WriteLine(e.ToString());
        }
    }
}
