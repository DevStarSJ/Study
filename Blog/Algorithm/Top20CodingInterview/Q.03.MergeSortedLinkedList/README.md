##Merge Sorted Linked List

How to merge two sorted linked list?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

정렬된 Linked List 2개를 Merge 하세요.

---

Merge Sort의 원리를 알고 있는지 확인하는 문제로 판단됩니다.

`C#`에서 제공하는 `LinkedList<T>`의 경우 이미 List에 속한 `LinkedListNode<T>`가 다른 List에 포함되는 것을 허가하지 않기 때문에 Value를 복사하여 새로운 Node를 생성하는 방법으로 구현해야 합니다.

이렇게 구현한 뒤에 원문의 정답을 보니 역시 그냥 여기저기서 Link가 가능한 Node란 것을 전제로 하였더군요.

그래서 별도의 간단한 (Q.02에서 구현하였던) LinkedNode를 이용하여 다시 풀어보았습니다.

###C Sharp using LinkedList<T>

```C#
using System.Collections.Generic;

class Program
{
    static LinkedList<int> Merge(ref LinkedList<int> listLeft, ref LinkedList<int> listRight)
    {
        LinkedList<int> listMerged = new LinkedList<int>();

        LinkedListNode<int> leftNode = listLeft.First;
        LinkedListNode<int> rightNode = listRight.First;

        while (leftNode != null || rightNode != null)
        {
            if (leftNode == null)
            {
                while (rightNode != null)
                {
                    listMerged.AddLast(rightNode.Value);
                    rightNode = rightNode.Next;
                }
                break;
            }
            else if (rightNode == null)
            {
                while (leftNode != null)
                {
                    listMerged.AddLast(leftNode.Value);
                    leftNode = leftNode.Next;
                }
                break;
            }
            else if (leftNode.Value >= rightNode.Value)
            {
                listMerged.AddLast(rightNode.Value);
                rightNode = rightNode.Next;
            }
            else
            {
                listMerged.AddLast(leftNode.Value);
                leftNode = leftNode.Next;
            }
        }

        return listMerged;
    }

    static void Main(string[] args)
    {
        LinkedList<int> nList1 = new LinkedList<int>( new int[] { 2, 4, 6, 8, 10, 15, 20 });
        LinkedList<int> nList2 = new LinkedList<int>( new int[] { 1, 3, 5, 7, 11, 13, 17, 20 });

        LinkedList<int> nList3 = Merge(ref nList1, ref nList2);

        LinkedListNode<int> node = nList3.First;

        while (node != null)
        {
            System.Console.Write(string.Format("{0,4}", node.Value));
            node = node.Next;
        }
        System.Console.WriteLine("");
    }
}
```
