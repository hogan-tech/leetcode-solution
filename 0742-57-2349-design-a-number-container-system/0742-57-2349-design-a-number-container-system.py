# time complexity: O(logn)
# space complexity: O(n)
from collections import defaultdict
from sortedcontainers import SortedSet


class NumberContainers:

    def __init__(self):
        self.numDict = defaultdict(SortedSet)
        self.idxDict = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if index in self.idxDict:
            lastNum = self.idxDict[index]
            self.numDict[lastNum].remove(index)
            if not self.numDict[lastNum]:
                del self.numDict[lastNum]

        self.idxDict[index] = number
        self.numDict[number].add(index)

    def find(self, number: int) -> int:
        if number in self.numDict and self.numDict[number]:
            return self.numDict[number][0]
        return -1


obj = NumberContainers()
print(obj.find(10))
obj.change(2, 10)
obj.change(1, 10)
obj.change(3, 10)
obj.change(5, 10)
print(obj.find(10))
obj.change(1, 20)
print(obj.find(10))
