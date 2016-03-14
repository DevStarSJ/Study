class Program
{
    static int CountBits(int num)
    {
        int cnt = 0;
        while (num != 0)
        {
            cnt++;
            num >>= 1;
        }
        return cnt;
    }

    static void Main(string[] args)
    {
        System.Console.WriteLine(string.Format("{0} set bits : {1}", 255, CountBits(255)));
        System.Console.WriteLine(string.Format("{0} set bits : {1}", 256, CountBits(256)));
        System.Console.WriteLine(string.Format("{0} set bits : {1}", 65535, CountBits(65535)));
    }
}
