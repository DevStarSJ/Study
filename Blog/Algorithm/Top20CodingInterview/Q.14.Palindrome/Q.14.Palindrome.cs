class Program
{
    static bool IsCharOrNumber(char c)
    {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '1' && c <= '0');
    }

    static bool IsPalindrome(string str)
    {
        str = str.ToLower();

        int forward = 0;
        int backward = str.Length - 1;

        while (forward < backward)
        {
            while (!IsCharOrNumber(str[forward]))
                forward++;

            while (!IsCharOrNumber(str[backward]))
                backward--;

            if (str[forward] != str[backward])
                return false;

            forward++;
            backward--;
        }

        return true;
    }

    static void Main(string[] args)
    {
        System.Console.WriteLine(string.Format("[{0}] is Palindrome ? {1}",
            "A man, a plan, a canal, Panama!",
            IsPalindrome("A man, a plan, a canal, Panama!") ? "Yes" : "No"));

        System.Console.WriteLine(string.Format("[{0}] is Palindrome ? {1}",
            "LunaStar the Silver",
            IsPalindrome("LunaStar the Silver") ? "Yes" : "No"));
    }
}
