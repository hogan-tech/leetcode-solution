# time complexity: O(1)
# space complexity: O(1)
from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2] or nums[1] + nums[2] <= nums[0] or nums[2] + nums[0] <= nums[1]:
            return "none"
        if nums[0] == nums[1] and nums[1] == nums[2]:
            return "equilateral"
        if nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"
        if nums[0] != nums[1] and nums[1] != nums[2]:
            return "scalene"


nums = [3, 3, 3]
print(Solution().triangleType(nums))
nums = [3, 4, 5]
print(Solution().triangleType(nums))
