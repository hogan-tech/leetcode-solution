from collections import defaultdict, deque
from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique = defaultdict()
        self.numsQ = deque()
        for num in nums:
            if num not in self.unique:
                self.unique[num] = 1
                self.numsQ.append(num)
            else:
                self.unique[num] += 1
                if num in self.numsQ:
                    self.numsQ.remove(num)

    def showFirstUnique(self) -> int:
        return self.numsQ[0] if self.numsQ else -1

    def add(self, value: int) -> None:
        if value in self.unique:
            self.unique[value] += 1
            if value in self.numsQ:
                self.numsQ.remove(value)
        else:
            self.unique[value] = 1
            self.numsQ.append(value)


firstUnique = FirstUnique([2, 3, 5])
print(firstUnique.showFirstUnique())
firstUnique.add(5)
print(firstUnique.showFirstUnique())
firstUnique.add(2)
print(firstUnique.showFirstUnique())
firstUnique.add(3)
print(firstUnique.showFirstUnique())

# firstUnique = FirstUnique([7, 7, 7, 7, 7, 7])
# print(firstUnique.showFirstUnique())
# firstUnique.add(7)
# firstUnique.add(3)
# firstUnique.add(3)
# firstUnique.add(7)
# firstUnique.add(17)
# print(firstUnique.showFirstUnique())

# firstUnique = FirstUnique([1])
# firstUnique.add(1)
# firstUnique.add(1)
# print(firstUnique.showFirstUnique())
