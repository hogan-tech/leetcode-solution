# time complexity: O(n^3)
# space complexity: O(1)
from typing import List


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
class UnionFind:
    def __init__(self, nums):
        self.parents = {num: num for num in nums}
        self.ranks = {num: 1 for num in nums}
        self.maxLength = 1

    def find(self, num):
        if num != self.parents[num]:
            self.parents[num] = self.find(self.parents[num])
        return self.parents[num]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return False
    
        if self.ranks[parent1] < self.ranks[parent2]:
            self.parents[parent1] = parent2
            self.ranks[parent2] += self.ranks[parent1]
        else:
            self.parents[parent2] = parent1
            self.ranks[parent1] += self.ranks[parent2]
            
        self.maxLength = max(self.maxLength, self.ranks[parent1], self.ranks[parent2])
        
        return True


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        uf = UnionFind(nums)
        for num in nums:
            if num + 1 in uf.parents:
                uf.union(num, num + 1)

        return uf.maxLength


nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(Solution().longestConsecutive(nums))
nums = [1, 0, 1, 2]
print(Solution().longestConsecutive(nums))
