using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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
