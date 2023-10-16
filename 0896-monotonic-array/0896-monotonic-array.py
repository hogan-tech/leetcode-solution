from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increaseNums = sorted(nums)
        decreaseNums = sorted(nums, reverse=True)
        return increaseNums == nums or decreaseNums == nums


nums = [1, 2, 2, 3]
print(Solution().isMonotonic(nums))
