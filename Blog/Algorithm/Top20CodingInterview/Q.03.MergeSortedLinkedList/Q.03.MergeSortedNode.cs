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