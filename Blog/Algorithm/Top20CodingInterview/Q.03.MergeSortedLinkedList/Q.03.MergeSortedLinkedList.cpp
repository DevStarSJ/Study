#include "stdafx.h"
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