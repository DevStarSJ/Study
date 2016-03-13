using System.Collections.Generic;

class Program
{
    static bool IsAnagram(string str1, string str2)
    {
        if (str1.Length != str2.Length)
            return false;
        
        string s1 = str1.ToLower();
        string s2 = str2.ToLower();

        Dictionary<char, int> dic = new Dictionary<char, int>();

        foreach(char c in s1)
        {
            if (dic.ContainsKey(c))
                dic[c] += 1;
            else
                dic.Add(c, 1);
        }

        foreach (char c in s2)
        {
            if (dic.ContainsKey(c))
            {
                dic[c] -= 1;
                if (dic[c] < 0)
                    return false;
            }
            else
                return false;
        }
        return true;
    }

    static void Main(string[] args)
    {
        System.Console.WriteLine(IsAnagram("Duty", "TYDU"));
        System.Console.WriteLine(IsAnagram("LunaStar", "Demilune"));
    }
}

