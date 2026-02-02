# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List
from sortedcontainers import SortedList


class Container:
    def __init__(self, k: int):
        self.k = k
        self.st1 = SortedList()
        self.st2 = SortedList()
        self.sm = 0

    def adjust(self):
        while len(self.st1) < self.k and len(self.st2) > 0:
            x = self.st2[0]
            self.st1.add(x)
            self.st2.remove(x)
            self.sm += x

        while len(self.st1) > self.k:
            x = self.st1[-1]
            self.st2.add(x)
            self.st1.remove(x)
            self.sm -= x

    def add(self, x: int):
        if len(self.st2) > 0 and x >= self.st2[0]:
            self.st2.add(x)
        else:
            self.st1.add(x)
            self.sm += x
        self.adjust()

    def erase(self, x: int):
        if x in self.st1:
            self.st1.remove(x)
            self.sm -= x
        elif x in self.st2:
            self.st2.remove(x)
        self.adjust()

    def sum(self) -> int:
        return self.sm


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        counter = Container(k - 2)
        for i in range(1, k - 1):
            counter.add(nums[i])

        result = counter.sum() + nums[k - 1]
        for i in range(k, n):
            j = i - dist - 1
            if j > 0:
                counter.erase(nums[j])
            counter.add(nums[i - 1])
            result = min(result, counter.sum() + nums[i])

        return result + nums[0]


nums = [1, 3, 2, 6, 4, 2]
k = 3
dist = 3
print(Solution().minimumCost(nums, k, dist))
nums = [10, 1, 2, 2, 2, 1]
k = 4
dist = 3
print(Solution().minimumCost(nums, k, dist))
nums = [10, 8, 18, 9]
k = 3
dist = 1
print(Solution().minimumCost(nums, k, dist))
