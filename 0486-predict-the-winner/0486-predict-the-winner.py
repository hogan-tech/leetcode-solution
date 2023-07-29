from functools import lru_cache
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def maxDiff(left, right):
            if left == right:
                return nums[left]
            return max(nums[left] - maxDiff(left + 1, right), nums[right] - maxDiff(left, right - 1))

        return maxDiff(0, len(nums)-1) >= 0