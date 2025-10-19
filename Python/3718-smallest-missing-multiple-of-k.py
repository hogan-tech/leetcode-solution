# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numSet = set(nums)
        for num in range(1, 100000):
            if num * k not in numSet:
                return num * k


nums = [8, 2, 3, 4, 6]
k = 2
print(Solution().missingMultiple(nums, k))
nums = [1, 4, 7, 10, 15]
k = 5
print(Solution().missingMultiple(nums, k))
