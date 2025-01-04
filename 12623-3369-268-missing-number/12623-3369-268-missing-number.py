# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            value = nums[i]
            if value < len(nums) and value != nums[value]:
                nums[i], nums[value] = nums[value], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(Solution().missingNumber(nums))
nums = [3, 0, 1]
print(Solution().missingNumber(nums))
nums = [0, 1]
print(Solution().missingNumber(nums))
