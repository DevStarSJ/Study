##Check Armstrong number

Check if a number is Armstrong number or not? 

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

입력받은 숫자가 암스트롱 넘버인지 확인하세요.

---

암스트롱 넘버란 각 자리의 1자리수를 3제곱한것을 모두 더한 합이 원래수와 같은 것을 뜻합니다.  

자세한 내용은 아래 Link를 참고하세요.

<http://everything2.net/index.pl?node_id=1407017&displaytype=printable&lastnode_id=1407017>

###C Sharp

```C#
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
```
