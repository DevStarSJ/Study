##Count Set Bits

Write a function to count a total number of set bits in a 32 bit Integer?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

32bit Int 값을 받아서 몇 Bit를 사용중인지 카운트하세요.

---

Shift 연산자 ( >>, << ) 만 사용할 수 있으면 풀 수 있습니다.  

만약 문제가 전체 사용하는 Bit가 아니라 1로 Set된 Bit가 몇개인지 묻는다면 Bit 연산자 ( &, | )를 사용해서 비교하면 됩니다.

###C Sharp

```C#
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
```
