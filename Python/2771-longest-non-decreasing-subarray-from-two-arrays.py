# time complexity: O(n)
# spaec complexity: O(n)
from functools import lru_cache
from typing import List


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache
        def dp(i: int, prev: int):
            if i == len(nums1):
                return 0
            result = 0
            if prev == 0:
                result = dp(i + 1, prev)
            if nums1[i] >= prev:
                result = max(result, 1 + dp(i + 1, nums1[i]))
            if nums2[i] >= prev:
                result = max(result, 1 + dp(i + 1, nums2[i]))
            return result
        return dp(0, 0)


nums1 = [2, 3, 1]
nums2 = [1, 2, 1]
print(Solution().maxNonDecreasingLength(nums1, nums2))
