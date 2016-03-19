import java.util.*;

public class LinkedNode<T> {
	
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

	public static void main(String[] args) {
		LinkedNode<String> node1 = new LinkedNode<String>("Luna");
		LinkedNode<String> node2 = new LinkedNode<String>("Star");
		LinkedNode<String> node3 = new LinkedNode<String>("Silver");
		LinkedNode<String> node4 = new LinkedNode<String>("Luna");
		
		node1.SetNext(node2);
		node2.SetNext(node3);
		node3.SetNext(node4);
		
		System.out.println(node2.DetectCirculation() == true ? "Detect Circulation" : "No Circulation");
		
		node3.SetNext(node2);
		
		System.out.println(node1.DetectCirculation() == true ? "Detect Circulation" : "No Circulation");

	}
}
