##Merge Sorted Linked List

How to merge two sorted linked list?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

정렬된 Linked List 2개를 Merge 하세요.

---

Merge Sort의 원리를 알고 있는지 확인하는 문제로 판단됩니다.

`C#`에서 제공하는 `LinkedList<T>`의 경우 이미 List에 속한 `LinkedListNode<T>`가 다른 List에 포함되는 것을 허가하지 않기 때문에 Value를 복사하여 새로운 Node를 생성하는 방법으로 구현해야 합니다.

이렇게 구현한 뒤에 원문의 정답을 보니 역시 그냥 여기저기서 Link가 가능한 Node란 것을 전제로 하였더군요.

그래서 별도의 간단한 (Q.02에서 구현하였던) LinkedNode에 함수몇개를 추가하여 풀어보았습니다.

###C# 

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

        while(findFirst._previous != null)
        {
            findFirst = findFirst._previous;
        }

        return findFirst;
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
        System.Console.ReadKey();
    }
}
```

###C++
```C++
#include <iostream>
#include <vector>
#include <exception>

class exception_notSortedNode : public std::exception
{
public:
	const char * what() const throw()
	{
		return "Not Sorted Node";
	}
};

class exception_detectingCirculationNode : public std::exception
{
public:
	const char * what() const throw()
	{
		return "Detecting Circulation Node";
	}
};

template <typename T>
class LinkedNode
{
public:
	T m_value;
	LinkedNode* m_pPrevious = nullptr;
	LinkedNode* m_pNext = nullptr;

	LinkedNode<T>(T p_value)
	{
		m_value = p_value;
	}

	void SetPrevious(LinkedNode* p_node)
	{
		m_pPrevious = p_node;
		p_node->m_pNext = this;
	}

	void SetNext(LinkedNode* p_node)
	{
		m_pNext = p_node;
		p_node->m_pPrevious = this;
	}

	bool DetectCirculation()
	{
		std::vector<LinkedNode*> vVisitedNodes{ this };

		LinkedNode* traveling = m_pPrevious;
		while (traveling != nullptr)
		{
			for (LinkedNode* visited : vVisitedNodes)
			{
				if (traveling == visited)
					return true;
			}
			vVisitedNodes.push_back(traveling);
			traveling = traveling->m_pPrevious;
		}

		traveling = m_pNext;
		while (traveling != nullptr)
		{
			for (LinkedNode* visited : vVisitedNodes)
			{
				if (traveling == visited)
					return true;
			}
			vVisitedNodes.push_back(traveling);
			traveling = traveling->m_pNext;
		}

		return false;
	}

	LinkedNode<T>* GetFirstNode()
	{
		LinkedNode<T>* findFirst = this;

		while (findFirst->m_pPrevious != nullptr)
		{
			findFirst = findFirst->m_pPrevious;
		}

		return findFirst;
	}

	bool IsSorted()
	{
		if (DetectCirculation())
			throw exception_detectingCirculationNode();

		LinkedNode<T>* traveling = GetFirstNode();

		while (traveling->m_pNext != nullptr)
		{
			if (traveling->m_value > traveling->m_pNext->m_value)
				return false;

			traveling = traveling->m_pNext;
		}

		return true;
	}

	static LinkedNode<T>* MergeSortedNodes(LinkedNode<T>* p_node1, LinkedNode<T>* p_node2)
	{
		if (p_node1 != nullptr && !p_node1->IsSorted())
			throw exception_notSortedNode();

		if (p_node2 != nullptr && !p_node2->IsSorted())
			throw exception_notSortedNode();

		if (p_node1 == nullptr)
			return p_node2->GetFirstNode();

		if (p_node2 == nullptr)
			return p_node1->GetFirstNode();

		LinkedNode<T>* node1 = p_node1->GetFirstNode();
		LinkedNode<T>* node2 = p_node2->GetFirstNode();
		LinkedNode<T>* first = nullptr;
		LinkedNode<T>* traveling = nullptr;

		if (node1->m_value <= node2->m_value)
		{
			first = node1;
			traveling = node1;
			node1 = node1->m_pNext;
		}
		else
		{
			first = node2;
			traveling = node2;
			node2 = node2->m_pNext;
		}

		while (node1 != nullptr && node2 != nullptr)
		{
			if (node1->m_value <= node2->m_value)
			{
				traveling->SetNext(node1);
				traveling = traveling->m_pNext;
				node1 = node1->m_pNext;
				if (node1 == nullptr)
				{
					traveling->SetNext(node2);
					break;
				}
			}
			else
			{
				traveling->SetNext(node2);
				traveling = traveling->m_pNext;
				node2 = node2->m_pNext;
				if (node2 == nullptr)
				{
					traveling->SetNext(node1);
					break;
				}
			}
		}

		return first;
	}

};

void main()
{
	LinkedNode<int> node1(1);
	LinkedNode<int> node2(3);
	LinkedNode<int> node3(5);
	LinkedNode<int> node4(6);
	node1.SetNext(&node2);
	node2.SetNext(&node3);
	node3.SetNext(&node4);

	LinkedNode<int> node5(2);
	LinkedNode<int> node6(4);
	LinkedNode<int> node7(8);
	LinkedNode<int> node8(9);
	node5.SetNext(&node6);
	node6.SetNext(&node7);
	node7.SetNext(&node8);

	LinkedNode<int>* sorted = LinkedNode<int>::MergeSortedNodes(&node3, &node8);
	LinkedNode<int>* traveling = sorted;

	while (traveling != nullptr)
	{
		int value = traveling->m_value;
		std::cout << value << " ";
		traveling = traveling->m_pNext;
	}

	std::cout << std::endl;
}
```

###Python
```python
class exceptionDetectingCirculation(Exception):
    def __init__(self):
        self.value = "Detecting Circulation"

    def __str__(self):
        return self.value

class exceptionNotSorted(Exception):
    def __init__(self):
        self.value = "Not Sorted"

    def __str__(self):
        return self.value

class Node:
    def __init__(self, value):
        self.value = value
        self._previous = None
        self._next = None

    def SetPrevious(self, node):
        self._previous = node
        node._next = self

    def SetNext(self, node):
        self._next = node
        node._previous = self

    def GetPrevious(self):
        return self._previous

    def GetNext(self):
        return self._next

    def DetectCirculation(self):
        vVisitedNodes = [ self ]

        traveling = self._previous

        while traveling is not None:
            for visited in vVisitedNodes:
                if traveling == visited:
                    return True
            vVisitedNodes.append(traveling)
            traveling = traveling._previous

        traveling = self._next
        
        while traveling is not None:
            for visited in vVisitedNodes:
                if traveling == visited:
                    return True
            vVisitedNodes.append(traveling)
            traveling = traveling._next

        return False
    
    def GetFirst(self):
        if self.DetectCirculation():
            raise exceptionDetectingCirculation
        
        traveling = self
        while traveling._previous != None:
            traveling = traveling._previous
        return traveling
        
    def IsSorted(self):
        traveling = self.GetFirst()
        while traveling._next != None:
            if traveling.value > traveling._next.value:
                return False
            traveling = traveling._next
        return True
    
    def MergeSortedNodes(self, other):
        if other != None and other.IsSorted() == False:
            raise exceptionNotSorted
        if self.IsSorted() == False:
            raise exceptionNotSorted
        
        node1 = self.GetFirst()
        
        if other == None:
            return node1
        
        node2 = other.GetFirst()
        
        first = node1
        
        if node1.value <= node2.value:
            node1 = node1._next
        else:
            first = node2
            node2 = node2._next
        
        traveling = first
        
        while node1 != None and node2 != None:
            
            if node1.value <= node2.value:
                
                traveling.SetNext(node1)
                traveling = traveling._next
                node1 = node1._next
                
                if node1 == None:
                    traveling.SetNext(node2)
                    break
                
            else:
                
                traveling.SetNext(node2)
                traveling = traveling._next
                node2 = node2._next
                
                if node2 == None:
                    traveling.SetNext(node1)
                    break
            
        return first
        
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node4 = Node(6)
    node1.SetNext(node2)
    node2.SetNext(node3)
    node3.SetNext(node4)
    
    node5 = Node(2)
    node6 = Node(4)
    node7 = Node(8)
    node8 = Node(9)
    node5.SetNext(node6)
    node6.SetNext(node7)
    node7.SetNext(node8)
    
    mergeSorted = node2.MergeSortedNodes(node7)
    
    while mergeSorted != None:
        print(mergeSorted.value)
        mergeSorted = mergeSorted.GetNext()
```
