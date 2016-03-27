import java.util.*;

public class LinkedNode<T extends Comparable<T>> {
	
	public T value;
	private LinkedNode<T> _previous = null;
	private LinkedNode<T> _next = null;
	
	public LinkedNode(T initValue){
		value = initValue;
	}
	
	public void SetPrevious(LinkedNode<T> prevNode)
	{
		_previous = prevNode;
		prevNode._next = this;
	}
	
	public void SetNext(LinkedNode<T> nextNode)
	{
		_next = nextNode;
		nextNode._previous = this;
	}
	
	public LinkedNode<T> GetPrevious() {
		return _previous;
	}
	
	public LinkedNode<T> GetNext() {
		return _next;
	}
	
	public boolean DetectCirculation()
	{
		ArrayList<LinkedNode<T>> visitedNodes =  new ArrayList<LinkedNode<T>>();
		visitedNodes.add(this);
		
		LinkedNode<T> traveling = _previous;
		
		while(traveling != null)
		{
			for (LinkedNode<T> visitedNode : visitedNodes)
			{
				if (traveling == visitedNode)
					return true;
			}
			visitedNodes.add(traveling);
			traveling = traveling._previous;
		}
		
		traveling = _next;
		
		while(traveling != null)
		{
			for (LinkedNode<T> visitedNode : visitedNodes)
			{
				if (traveling == visitedNode)
					return true;
			}
			visitedNodes.add(traveling);
			traveling = traveling._next;
		}
		
		return false;
	}
	
	public LinkedNode<T> GetFirst() throws Exception {
		if (DetectCirculation())
			throw new Exception("Detecting Circulation");
		
		LinkedNode<T> traveling = this;
		
		while (traveling._previous != null)
		{
			traveling = traveling._previous;
		}
		
		return traveling;
	}
	
	public boolean IsSorted() throws Exception {
		
		LinkedNode<T> traveling = GetFirst();
		
		while (traveling._next != null)
		{
			if (traveling.value.compareTo(traveling._next.value) > 0) // traveling > traveling._next
				return false;
			
			traveling = traveling._next;
		}
		
		return true;
	}
	
	public LinkedNode<T> MergeSortedNodes(LinkedNode<T> other) throws Exception
	{
		if (!IsSorted())
			throw new Exception("Not Sorted");
		
		if (other != null && !other.IsSorted())
			throw new Exception("Not Sorted");
		
		LinkedNode<T> node1 = GetFirst();
		
		if (other == null)
			return node1;
		
		LinkedNode<T> node2 = other.GetFirst();
		
		LinkedNode<T> first = node1;
		if (node1.value.compareTo(node2.value) <= 0) // node1 <= node2
		{
			node1 = node1._next;
		}
		else
		{
			first = node2;
			node2 = node2._next;
		}
		
		LinkedNode<T> traveling = first;
		
		while (node1 != null && node2 != null)
		{
			if (node1.value.compareTo(node2.value) > 0) // node1 > node2
			{
				traveling.SetNext(node2);
				traveling = traveling._next;
				
				node2 = node2._next;
				if (node2 == null)
				{
					traveling.SetNext(node1);
					break;
				}
			}
			else // node1 <= node2
			{
				traveling.SetNext(node1);
				traveling = traveling._next;
				
				node1 = node1._next;
				if (node1 == null)
				{
					traveling.SetNext(node2);
					break;
				}
			}
		}
		
		return first;
	}

	public static void main(String[] args) {
		
		LinkedNode<Integer> node1 = new LinkedNode<Integer>(1);
		LinkedNode<Integer> node2 = new LinkedNode<Integer>(3);
		LinkedNode<Integer> node3 = new LinkedNode<Integer>(5);
		LinkedNode<Integer> node4 = new LinkedNode<Integer>(6);
		
		node1.SetNext(node2);
		node2.SetNext(node3);
		node3.SetNext(node4);
		
		LinkedNode<Integer> node5 = new LinkedNode<Integer>(2);
		LinkedNode<Integer> node6 = new LinkedNode<Integer>(4);
		LinkedNode<Integer> node7 = new LinkedNode<Integer>(8);
		LinkedNode<Integer> node8 = new LinkedNode<Integer>(9);
		
		node5.SetNext(node6);
		node6.SetNext(node7);
		node7.SetNext(node8);
		
		LinkedNode<Integer> mergeSorted = null;
		try {
			mergeSorted = node2.MergeSortedNodes(node7);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		while (mergeSorted != null)
		{
			System.out.println(mergeSorted.value);
			mergeSorted = mergeSorted.GetNext();
		}
	}
}
