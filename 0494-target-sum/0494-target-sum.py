from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)
        if abs(target) > total:
            return 0
        dp = [[0] * (2 * total + 1) for _ in range(len(nums))]
        dp[0][nums[0] + total] = 1
        dp[0][-nums[0] + total] += 1
        for i in range(1, len(nums)):
            for itemSum in range(-total, total + 1):
                if (dp[i - 1][itemSum + total] > 0):
                    dp[i][itemSum + nums[i] + total] += dp[i-1][itemSum + total]
                    dp[i][itemSum - nums[i] + total] += dp[i-1][itemSum + total]
        print(dp)
        return dp[len(nums) - 1][target + total]


nums = [1, 1, 1, 1, 1]
target = 3
print(Solution().findTargetSumWays(nums, target))
