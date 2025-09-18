class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        dp = [0]
        for i in range(len(nums)):
            dp.append(max((nums[j] + j for j in range(dp[i] + 1))))
            if dp[i + 1] >= len(nums) - 1:
                break
        return len(dp) - 1