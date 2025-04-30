from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftPrefix = [0 for _ in range(len(nums))]
        rightPrefix = [0 for _ in range(len(nums))]
        leftPrefix[0] = nums[0]
        rightPrefix[-1] = nums[-1]
        for i in range(1, len(nums)):
            leftPrefix[i] = max(leftPrefix[i - 1], nums[i])
        for i in range(len(nums) - 2, -1, -1):
            rightPrefix[i] = min(rightPrefix[i + 1], nums[i])
        
        for i in range(1,len(nums)):
            if leftPrefix[i - 1] <= rightPrefix[i]:
                return i


nums = [5, 0, 3, 8, 6]
print(Solution().partitionDisjoint(nums))
nums = [1, 1, 1, 0, 6, 12]
print(Solution().partitionDisjoint(nums))
