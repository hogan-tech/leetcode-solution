# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        targetIdx = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= targetIdx:
                targetIdx = i
        if targetIdx == 0:
            return True
        return False


nums = [2, 3, 1, 1, 4]
print(Solution().canJump(nums))
nums = [3, 2, 1, 0, 4]
print(Solution().canJump(nums))
