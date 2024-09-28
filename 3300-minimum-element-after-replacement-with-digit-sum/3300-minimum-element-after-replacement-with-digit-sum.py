# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def findSum(self, num: int):
        if num == 0:
            return 0
        return int(num % 10) + self.findSum(num / 10)

    def minElement(self, nums: List[int]) -> int:
        minValue = float('inf')
        for i, num in enumerate(nums):
            nums[i] = self.findSum(num)
            minValue = min(minValue, nums[i])
        return minValue


nums = [999, 19, 199]
print(Solution().minElement(nums))
