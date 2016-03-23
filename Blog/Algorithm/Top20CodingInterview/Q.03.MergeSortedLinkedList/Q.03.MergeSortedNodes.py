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