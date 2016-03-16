class NoMajority(Exception):
    def __init__(self):
        self.value = "No Majority"

    def __str__(self):
        return self.value

def FindMajority(listNumbers):
    mExsitingNumbers = dict()
    nMajority = len(listNumbers) / 2
    for nNumber in listNumbers:
        if nNumber in mExsitingNumbers:
            mExsitingNumbers[nNumber] += 1
            if mExsitingNumbers[nNumber] >= nMajority:
                return nNumber
        else:
            mExsitingNumbers[nNumber] = 1
    raise NoMajority

listNumbers = [ 1,2,3,4,5,6,7,8,9,0]

try:
    print(FindMajority(listNumbers))
except NoMajority as err:
    print(err)

try:
    print(FindMajority([1,2,3,4,4,4,4,6,3,4]))
except NoMajority as err:
    print(err)
