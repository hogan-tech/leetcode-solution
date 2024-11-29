# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rigthSum = sum(nums)
        for i in range(len(nums)):
            rigthSum -= nums[i]
            if rigthSum == leftSum:
                return i
            leftSum += nums[i]
        return -1


nums = [1, 7, 3, 6, 5, 6]
print(Solution().pivotIndex(nums))
