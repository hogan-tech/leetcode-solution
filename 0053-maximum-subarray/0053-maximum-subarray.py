class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = -100000
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum < nums[i]:
                sum = nums[i]
            maxNum = max(sum, maxNum)
        return maxNum