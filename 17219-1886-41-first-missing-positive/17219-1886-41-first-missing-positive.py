# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            value = nums[i] - 1
            if 0 <= value < n and nums[i] != nums[value]:
                nums[value], nums[i] = nums[i], nums[value]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


nums = [1, 2, 0]
print(Solution().firstMissingPositive(nums))
nums = [3, 4, -1, 1]
print(Solution().firstMissingPositive(nums))
nums = [7, 8, 9, 11, 12]
print(Solution().firstMissingPositive(nums))
