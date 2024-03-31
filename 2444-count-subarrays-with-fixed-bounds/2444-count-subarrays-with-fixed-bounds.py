# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        badIdx = leftIdx = rightIdx = -1
        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                badIdx = i
            if num == minK:
                leftIdx = i
            if num == maxK:
                rightIdx = i
            res += max(0, min(leftIdx, rightIdx) - badIdx)
        return res


nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5

print(Solution().countSubarrays(nums, minK, maxK))
