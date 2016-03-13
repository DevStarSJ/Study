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
