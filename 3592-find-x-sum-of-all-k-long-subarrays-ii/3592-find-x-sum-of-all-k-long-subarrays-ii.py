# time complexity: O(nlogk)
# space complexity: O(k)
from collections import defaultdict
from sortedcontainers import SortedList
from typing import List


class Helper:
    def __init__(self, x):
        self.x = x
        self.result = 0
        self.large = SortedList()
        self.small = SortedList()
        self.occ = defaultdict(int)

    def insert(self, num):
        if self.occ[num] > 0:
            self.internalRemove((self.occ[num], num))
        self.occ[num] += 1
        self.internalInsert((self.occ[num], num))

    def remove(self, num):
        self.internalRemove((self.occ[num], num))
        self.occ[num] -= 1
        if self.occ[num] > 0:
            self.internalInsert((self.occ[num], num))

    def get(self):
        return self.result

    def internalInsert(self, p):
        if len(self.large) < self.x or p > self.large[0]:
            self.result += p[0] * p[1]
            self.large.add(p)
            if len(self.large) > self.x:
                to_remove = self.large[0]
                self.result -= to_remove[0] * to_remove[1]
                self.large.remove(to_remove)
                self.small.add(to_remove)
        else:
            self.small.add(p)

    def internalRemove(self, p):
        if p >= self.large[0]:
            self.result -= p[0] * p[1]
            self.large.remove(p)
            if self.small:
                to_add = self.small[-1]
                self.result += to_add[0] * to_add[1]
                self.small.remove(to_add)
                self.large.add(to_add)
        else:
            self.small.remove(p)


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        helper = Helper(x)
        result = []

        for i in range(len(nums)):
            helper.insert(nums[i])
            if i >= k:
                helper.remove(nums[i - k])
            if i >= k - 1:
                result.append(helper.get())

        return result
