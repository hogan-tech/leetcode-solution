from typing import Counter, List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        maxValue = -1
        for key, value in Counter(nums).items():
            if value == 1:
                maxValue = max(maxValue, key)
        return maxValue


nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
print(Solution().largestUniqueNumber(nums))
