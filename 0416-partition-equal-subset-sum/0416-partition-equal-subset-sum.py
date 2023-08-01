from functools import lru_cache
from typing import List, Tuple


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(nums: Tuple[int], n: int, subSum: int):
            if subSum == 0:
                return True
            if n == 0 or subSum < 0:
                return False
            result = dfs(nums, n-1, subSum-nums[n-1]) or dfs(nums, n-1, subSum)
            return result

        partitionSum = sum(nums) // 2
        if sum(nums) % 2:
            return False

        return dfs(tuple(nums), len(nums)-1, partitionSum)