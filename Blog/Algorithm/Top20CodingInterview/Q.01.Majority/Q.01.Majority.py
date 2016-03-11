class NoMajority(Exception):
    def __init__(self):
        self.value = "No Majority"

    def __str__(self):
        return self.value


def FindMajority(inList):
    mFind = dict()
    nMajority = len(inList) / 2
    for nElement in inList:
        if nElement in mFind:
            mFind[nElement] += 1
            if mFind[nElement] >= nMajority:
                return nElement
        else:
            mFind[nElement] = 1
    raise NoMajority

list = [ 1,2,3,4,5,6,7,8,9,0]

try:
    print(FindMajority(list))
except NoMajority as err:
    print(err)

try:
    print(FindMajority([1,2,3,4,4,4,4,6,3,4]))
except NoMajority as err:
    print(err)
