class Program
{
    static string RemoveDiplicateChar(string str)
    {
        string result = string.Empty;

        foreach(char c in str)
        {
            if (result.IndexOf(c) != -1)
                continue;
            result += c;
        }

        return result;
    }
    static void Main(string[] args)
    {
        string str1 = "I love you";
        System.Console.WriteLine(string.Format("{0} : {1}", str1, RemoveDiplicateChar(str1)));
    }
}
