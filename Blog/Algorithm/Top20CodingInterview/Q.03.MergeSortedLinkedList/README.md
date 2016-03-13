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

###C Sharp with Implementation of Node

```C#
class LinkedNode<T> : object
{
    public T Value { set; get; }

    private LinkedNode<T> _previous = null;
    private LinkedNode<T> _next = null;

    public LinkedNode<T> Previous
    {
        set
        {
            _previous = value;
            value._next = this;
        }
        get
        {
            return _previous;
        }
    }

    public LinkedNode<T> Next
    {
        set
        {
            _next = value;
            value._previous = this;
        }
        get
        {
            return _next;
        }
    }

    public LinkedNode(T value)
    {
        Value = value;
    }

    public static LinkedNode<int> Merge(LinkedNode<int> list1, LinkedNode<int> list2)
    {
        LinkedNode<int> first = null;
        LinkedNode<int> current = null;

        LinkedNode<int> node1 = list1;
        LinkedNode<int> node2 = list2;

        if (node1 == null)
        {
            return node2;
        }
        else if (node2 == null)
        {
            return node1;
        }
        if (node1.Value >= node2.Value)
        {
            first = node2;
            current = first;
            node2 = node2.Next;
        }
        else
        {
            first = node1;
            current = first;
            node1 = node1.Next;
        }

        while (node1 != null && node2 != null)
        {
            if (node1.Value >= node2.Value)
            {
                current.Next = node2;
                current = current.Next;
                node2 = node2.Next;
                if (node2 == null)
                {
                    current.Next = node1;
                    break;
                }
            }
            else
            {
                current.Next = node1;
                current = current.Next;
                node1 = node1.Next;
                if (node1 == null)
                {
                    current.Next = node2;
                    break;
                }
            }
        }
        return first;
    }
}

class Program
{
    static void Main(string[] args)
    {
        LinkedNode<int> node1 = new LinkedNode<int>(1);
        LinkedNode<int> node2 = new LinkedNode<int>(3);
        LinkedNode<int> node3 = new LinkedNode<int>(5);
        LinkedNode<int> node4 = new LinkedNode<int>(6);
        node1.Next = node2;
        node2.Next = node3;
        node3.Next = node4;

        LinkedNode<int> node5 = new LinkedNode<int>(2);
        LinkedNode<int> node6 = new LinkedNode<int>(4);
        LinkedNode<int> node7 = new LinkedNode<int>(8);
        LinkedNode<int> node8 = new LinkedNode<int>(9);
        node5.Next = node6;
        node6.Next = node7;
        node7.Next = node8;

        LinkedNode<int> ret = LinkedNode<int>.Merge(node1, node5);

        while (ret != null)
        {
            System.Console.Write(string.Format("{0,4}", ret.Value));
            ret = ret.Next;
        }
        System.Console.WriteLine("");
    }
}
```
