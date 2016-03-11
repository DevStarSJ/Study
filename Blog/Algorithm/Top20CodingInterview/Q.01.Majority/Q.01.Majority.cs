using System;
using System.Collections.Generic;
using System.Linq;

namespace Q01Majority
{
    class Program
    {
        private static int FindMajority(List<int> p_nList)
        {
            int nMajority = p_nList.Count() / 2;

            Dictionary<int, int> mFind = new Dictionary<int, int>();

            foreach(int nElement in p_nList)
            {
                if (mFind.ContainsKey(nElement))
                {
                    mFind[nElement] += 1;
                    if (mFind[nElement] >= nMajority)
                    {
                        return nElement;
                    }
                }
                else
                {
                    mFind.Add(nElement, 1);
                }
            }

            throw new Exception("There is no Majority");
        }

        static void Main(string[] args)
        {
            List<int> list = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

            try
            {
                int nRet = FindMajority(list);

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
}
