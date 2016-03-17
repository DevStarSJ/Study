##Detect Circulation

How to detect a cycle in singly linked list?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

Linked List에서 순환 참조를 탐지하세요.

통상적으로 Library로 제공되는 Linked List는 Circulation 자체를 허용하지 않습니다.  

그래서 기본 기능만 하는 Linked List를 간단하게 구현한 다음 `DetectCirculation()`이라는 함수로 구현하였습니다.

원문의 정답과는 차이가 있지만 저는 다음의 방법으로 구현하였습니다.  

Linked List Node자체를 Object로 생성하여 해당 Node중 아무곳에서나 순환 참조를 탐지할 수 있도록 구현하였습니다.

- 자신의 Node를 기준으로 앞방향, 뒷방향으로 Node들을 방문한다.
- 한번 방문한 Node를 별도의 List에 저장해 둔다.
- 새로 방문한 Node를 이미 방문한 적이 있는 Node List와 비교한다. 이미 방문한 Node라면 `return true`
- 더 이상 방문할 Node가 없다면 `return fasle`

###C\# 

```C#
using System.Collections.Generic;

namespace Q02DetectCircular
{
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
    }

    class Program
    {
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
```

###C++

```C++
#include <iostream>
#include <vector>

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
};

void main()
{
	LinkedNode<std::string> node1("Luna");
	LinkedNode<std::string> node2("Star");
	LinkedNode<std::string> node3("Dev");
	LinkedNode<std::string> node4("Luna");

	node1.SetNext(&node2);
	node3.SetNext(&node4);
	node3.SetPrevious(&node2);

	std::cout << node3.DetectCirculation() << std::endl;

	node4.SetNext(&node2);

	std::cout << node1.DetectCirculation() << std::endl;
}
```

###Python

```Python
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

node1 = Node("Luna")
node2 = Node("Star")
node3 = Node("Silver")
node4 = Node("Luna")

node1.SetNext(node2)
node2.SetNext(node3)
node3.SetNext(node4)

print(node2.DetectCirculation())

node4.SetNext(node2)

print(node1.DetectCirculation())
```
