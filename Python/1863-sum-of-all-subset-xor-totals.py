from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = 0
        for i in range(1 << n):
            subsetXor = 0
            for j in range(n):
                if i & (1 << j):
                    subsetXor ^= nums[j]
            totalSum += subsetXor
        return totalSum


nums = [1, 3]
print(Solution().subsetXORSum(nums))
