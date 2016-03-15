##Find end of 3th element in single pass linked list

How to find the 3rd element from end, in a singly linked, in a single pass?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

한쪽 방향으로만 진행가능한 Linked List에서 끝에서 3번째 값을 찾으세요.

---

현재 진행중인 Node에서 3번째 전의 값을 어딘가에 저장하면서 진행하면 쉽게 찾을 수 있습니다.

방법으로는 여러가지가 있을 수 있습니다.

원문 Link의 방법대로 node 2개를 선언해서 그 중 하나는 head로 부터 3칸을 먼저 진행한 뒤에 같이 가는 방법도 있구요.  

저는 queue의 size를 3으로 유지하면서 모든 진행이 끝난뒤 queue의 처음값을 return하였습니다.

###C Sharp

```C#
using System.Collections.Generic;

class Program
{
    static T FindEndOf3th<T>(LinkedList<T> list)
    {
        Queue<T> queue = new Queue<T>();

        LinkedListNode<T> node = list.First;

        while (node != null)
        {
            queue.Enqueue(node.Value);

            if (queue.Count > 3)
                queue.Dequeue();

            node = node.Next;
        }
        return queue.Dequeue();
    }
    static void Main(string[] args)
    {
        LinkedList<int> list = new LinkedList<int>();
        list.AddLast(1);
        list.AddLast(2);
        list.AddLast(3);
        list.AddLast(4);
        list.AddLast(5);

        System.Console.WriteLine(FindEndOf3th<int>(list));
    }
}
```
