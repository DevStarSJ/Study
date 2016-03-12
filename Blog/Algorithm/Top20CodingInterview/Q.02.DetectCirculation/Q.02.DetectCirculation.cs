using System;
using System.Collections.Generic;

namespace Q02DetectCircular
{
    class LinkedNode<T> : Object
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

        public bool DetectCirculation()
        {
            List<LinkedNode<T>> checkList = new List<LinkedNode<T>>();

            LinkedNode<T> node = Previous;
            while (node != null)
            {
                foreach (LinkedNode<T> Visited in checkList)
                    if (Visited == node)
                        return true;
                checkList.Add(node);
                node = node.Previous;
            }

            node = Next;
            while (node != null)
            {
                int nHash = node.GetHashCode();
                foreach (LinkedNode<T> Visited in checkList)
                    if (Visited == node)
                        return true;
                checkList.Add(node);
                node = node.Next;
            }

            return false;
        }
    }

    class Program
    {
        static bool DetectCircular(LinkedList<string> list)
        {
            List<int> checkList = new List<int>();

            LinkedListNode<string> node = list.First;
           
            while(node != null)
            {
                int nHash = node.GetHashCode();

                foreach(int nVisited in checkList)
                    if (nVisited == nHash)
                        return true;

                checkList.Add(nHash);
                node = node.Next;
            }

            return false;
        }

        static void Main(string[] args)
        {
            LinkedNode<string> node1 = new LinkedNode<string>("Luna");
            LinkedNode<string> node2 = new LinkedNode<string>("Star");
            LinkedNode<string> node3 = new LinkedNode<string>("Dev");
            LinkedNode<string> node4 = new LinkedNode<string>("Luna");

            node1.Next = node2;
            node3.Next = node4;
            node3.Previous = node2;

            System.Console.WriteLine(node3.DetectCirculation());

            node4.Next = node2;

            System.Console.WriteLine(node3.DetectCirculation());
        }
    }
}
