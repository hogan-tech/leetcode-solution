# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)
        for i in range(len(numSet) + 1):
            if i not in numSet:
                return i


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(Solution().missingNumber(nums))
