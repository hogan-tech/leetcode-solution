# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        minIncrement = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                increment = nums[i-1] - nums[i] + 1
                minIncrement += increment
                nums[i] = nums[i-1] + 1
        return minIncrement


nums = [3, 2, 1, 2, 1, 7]
print(Solution().minIncrementForUnique(nums))
