# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def triangleValid(a, b, c):
            return (a + b) > c and (b + c) > a and (a + c) > b
        nums = sorted(nums, reverse=True)
        for a, b, c in zip(nums, nums[1:], nums[2:]):
            if triangleValid(a, b, c):
                return a + b + c
        return 0


nums = [2, 1, 2]
print(Solution().largestPerimeter(nums))
nums = [1, 2, 1, 10]
print(Solution().largestPerimeter(nums))
nums = [3, 2, 3, 4]
print(Solution().largestPerimeter(nums))
