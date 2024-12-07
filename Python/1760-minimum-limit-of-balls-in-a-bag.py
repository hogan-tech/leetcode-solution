# time complexity: O(nlogk)
# space complexity: O(1)
import math
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)
        while left < right:
            middle = (left + right) // 2
            if self.isPossible(middle, nums, maxOperations):
                right = middle
            else:
                left = middle + 1
        return left

    def isPossible(self, maxBallsInBag: int, nums: List[int], maxOperations: int):
        totalOperations = 0
        for num in nums:
            operations = math.ceil(num / maxBallsInBag) - 1
            totalOperations += operations
            if totalOperations > maxOperations:
                return False
        return True


nums = [9]
maxOperations = 2
print(Solution().minimumSize(nums, maxOperations))
nums = [2, 4, 8, 2]
maxOperations = 4
print(Solution().minimumSize(nums, maxOperations))
