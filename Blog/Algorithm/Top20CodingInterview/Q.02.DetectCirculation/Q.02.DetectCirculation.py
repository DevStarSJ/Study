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
