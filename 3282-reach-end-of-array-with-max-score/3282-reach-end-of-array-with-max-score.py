# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        curr = 0
        prefix = 0

        for i, x in enumerate(nums):
            if i:
                curr += prefix
            prefix = max(prefix, x)

        return curr


nums = [1, 3, 1, 5]
print(Solution().findMaximumScore(nums))
