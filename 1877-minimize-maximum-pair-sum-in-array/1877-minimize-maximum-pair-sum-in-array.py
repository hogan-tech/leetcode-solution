from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = 0
        for i in range(len(nums)//2):
            maxSum = max(maxSum, nums[i] + nums[len(nums) - 1 - i])
        return maxSum


nums = [3, 5, 2, 3]
print(Solution().minPairSum(nums))
