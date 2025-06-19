# time complexity: O(m*n)
# space complexity: O(m*n)
from functools import lru_cache
from typing import List, Tuple


# Bottom Up
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        subSum = sum(nums) // 2
        dp = [[False for i in range(len(nums) + 1)] for j in range(subSum + 1)]
        for subSumIdx in range(0, len(nums) + 1):
            dp[0][subSumIdx] = True

        for subSumIdx in range(1, subSum + 1):
            for nIdx in range(1, len(nums) + 1):
                if nums[nIdx - 1] > subSumIdx:
                    dp[subSumIdx][nIdx] = dp[subSumIdx][nIdx-1]
                else:
                    dp[subSumIdx][nIdx] = dp[subSumIdx - nums[nIdx-1]][nIdx-1] or dp[subSumIdx][nIdx-1]
        return True

# Top Down
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(nums: Tuple[int], n: int, subSum: int):
            if subSum == 0:
                return True
            if n == 0 or subSum < 0:
                return False
            return dp(nums, n - 1, subSum - nums[n - 1]) or dp(nums, n - 1, subSum)
        partitionSum = sum(nums) // 2
        if sum(nums) % 2:
            return False
        return dp(tuple(nums), len(nums) - 1, partitionSum)


nums = [1, 5, 11, 5]
print(Solution().canPartition(nums))
nums = [1, 2, 3, 5]
print(Solution().canPartition(nums))
nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
        100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 97]
print(Solution().canPartition(nums))
