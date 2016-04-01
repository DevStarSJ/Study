##Q.18.Remove Duplicates In Sorted Linked List

How to remove duplicates from a sorted linked list?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

정렬된 Linked List에서 중복값을 제거하세요.

16번문제에서 만든 `LinkedNode<T>` class에 아래 1개의 method를 추가했습니다.

---

###C# 추가한 method

```C#
public void RemoveDuplicatesInSortedLinkedList()
{
    if (!IsSorted())
        throw new Exception("Not Sorted");

    LinkedNode<T> traveling = GetFisrt();

    while (traveling._next != null)
    {
        if (traveling.Value.CompareTo(traveling._next.Value) == 0)
        {
            traveling.Next = traveling._next._next;
        }
        traveling = traveling._next;
    }
}
```

###C# 전체 Code (Test 포함)
```C#
using System;
using System.Collections.Generic;

class LinkedNode<T> where T : IComparable
{
    public T Value { set; get; }

    private LinkedNode<T> _previous = null;
    private LinkedNode<T> _next = null;

    public LinkedNode<T> Previous
    {
        set
        {
            _previous = value;
            if (value != null)
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
            if (value != null)
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

    public bool DetectCirculation()
    {
        List<LinkedNode<T>> vVisitedNodes = new List<LinkedNode<T>>();
        vVisitedNodes.Add(this);

        LinkedNode<T> traveling = Previous;
        while (traveling != null)
        {
            foreach (LinkedNode<T> visited in vVisitedNodes)
                if (visited == traveling)
                    return true;
            vVisitedNodes.Add(traveling);
            traveling = traveling.Previous;
        }

        traveling = Next;
        while (traveling != null)
        {
            foreach (LinkedNode<T> Visited in vVisitedNodes)
                if (Visited == traveling)
                    return true;
            vVisitedNodes.Add(traveling);
            traveling = traveling.Next;
        }

        return false;
    }

    public LinkedNode<T> GetFisrt()
    {
        if (DetectCirculation())
            throw new Exception("Circulation Linked Node");
        LinkedNode<T> findFirst = this;

        while (findFirst._previous != null)
        {
            findFirst = findFirst._previous;
        }

        return findFirst;
    }

    public LinkedNode<T> GetLast()
    {
        if (DetectCirculation())
            throw new Exception("Circulation Linked Node");
        LinkedNode<T> findLast = this;

        while (findLast._next != null)
        {
            findLast = findLast._next;
        }

        return findLast;
    }

    public bool IsSorted()
    {
        LinkedNode<T> traveling = GetFisrt();

        while (traveling._next != null)
        {
            if (traveling.Value.CompareTo(traveling._next.Value) > 0)
                return false;
            traveling = traveling._next;
        }

        return true;
    }

    public static LinkedNode<T> Merge(LinkedNode<T> list1, LinkedNode<T> list2)
    {
        if (list1 != null && !list1.IsSorted())
            throw new Exception("No Sorted List Inserted : " + nameof(list1));

        if (list2 != null && !list2.IsSorted())
            throw new Exception("No Sorted List Inserted : " + nameof(list2));

        if (list1 == null)
        {
            return list2;
        }
        else if (list2 == null)
        {
            return list1;
        }

        LinkedNode<T> first = null;
        LinkedNode<T> current = null;

        LinkedNode<T> node1 = list1.GetFisrt();
        LinkedNode<T> node2 = list2.GetFisrt();

        if (node1.Value.CompareTo(node2.Value) >= 0)
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
            if (node1.Value.CompareTo(node2.Value) >= 0)
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

    public void Reverse()
    {
        LinkedNode<T> newFirst = GetLast();
        LinkedNode<T> travelingForward = newFirst;
        LinkedNode<T> travelingBackward = travelingForward._previous;

        while (travelingBackward != null)
        {
            travelingForward._next = travelingBackward;

            travelingForward = travelingForward._next;
            travelingBackward = travelingBackward._previous;
        }

        travelingForward._next = null;
        newFirst._previous = null;

        travelingForward = newFirst;
        while (travelingForward._next != null)
        {
            travelingForward.Next = travelingForward._next;
            travelingForward = travelingForward._next;
        }
    }

    public void RemoveDuplicatesInSortedLinkedList()
    {
        if (!IsSorted())
            throw new Exception("Not Sorted");

        LinkedNode<T> traveling = GetFisrt();

        while (traveling._next != null)
        {
            if (traveling.Value.CompareTo(traveling._next.Value) == 0)
            {
                traveling.Next = traveling._next._next;
            }
            traveling = traveling._next;
        }
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

        LinkedNode<int> node5 = new LinkedNode<int>(1);
        LinkedNode<int> node6 = new LinkedNode<int>(5);
        LinkedNode<int> node7 = new LinkedNode<int>(8);
        LinkedNode<int> node8 = new LinkedNode<int>(9);
        node5.Next = node6;
        node6.Next = node7;
        node7.Next = node8;

        LinkedNode<int> merged = LinkedNode<int>.Merge(node1, node5);

        merged.RemoveDuplicatesInSortedLinkedList();

        LinkedNode<int> ret = merged.GetFisrt();

        while (ret != null)
        {
            System.Console.Write(string.Format("{0,4}", ret.Value));
            ret = ret.Next;
        }
        System.Console.WriteLine("");
    }
}
```
