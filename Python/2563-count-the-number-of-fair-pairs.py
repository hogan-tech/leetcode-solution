# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lowerBound(nums, upper+1) - self.lowerBound(nums, lower)

    def lowerBound(self, nums: List[int], value: int) -> int:
        left, right = 0, len(nums) - 1
        result = 0
        while left <= right:
            if nums[left] + nums[right] < value:
                result += right - left
                left += 1
            else:
                right -= 1
        return result


nums = [0, 1, 7, 4, 4, 5]
lower = 3
upper = 6
print(Solution().countFairPairs(nums, lower, upper))

nums = [1, 7, 9, 2, 5]
lower = 11
upper = 11
print(Solution().countFairPairs(nums, lower, upper))
