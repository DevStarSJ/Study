##Swap Number without using additional memory

How to swap two numbers without using a temp variable, write code which is free from Integer overflow? 

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

추가로 변수를 사용하지 않고 두 숫자의 저장된 위치를 바꾸세요.

이 문제는 Programming skill을 묻는게 아니라 해법을 생각하게 하는 질문입니다.

방법은 2가지가 있습니다.

`+`나 `-`를 이용해도 되지만, 그럴 경우 overflow가 일어날 수가 있기 때문에 XOR연산(`^`)을 이용하면 됩니다.

###C Sharp

```C#
class Program
{
    static void Main(string[] args)
    {
        int a = 30593;
        int b = 13953093;

        a ^= b;
        b ^= a;
        a ^= b;

        System.Console.WriteLine(a);
        System.Console.WriteLine(b);
    }
}
```
