# time complexity: O(n^3)
# space complexity: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestStreak = 0
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                currentNum = num
                currentStreak = 1

                while currentNum + 1 in numSet:
                    currentNum += 1
                    currentStreak += 1

                longestStreak = max(longestStreak, currentStreak)

        return longestStreak

# time complexity: O(n)
# space complexity: O(n)
from typing import List


class UnionFind:
    def __init__(self, nums):
        self.parents = {num: num for num in nums}
        self.ranks = {num: 1 for num in nums}
        self.maxLength = 1

    def find(self, num):
        if num != self.parents[num]:
            self.parents[num] = self.find(self.parents[num])
        return self.parents[num]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX != parentY:
            if self.ranks[parentX] < self.ranks[parentY]:
                parentX, parentY = parentY, parentX
            self.parents[parentY] = parentX
            self.ranks[parentX] += self.ranks[parentY]
            self.maxLength = max(self.maxLength, self.ranks[parentX])


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        disjointSet = UnionFind(nums)
        for num in nums:
            if num + 1 in disjointSet.parents:
                disjointSet.union(num, num + 1)

        return disjointSet.maxLength





nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))
