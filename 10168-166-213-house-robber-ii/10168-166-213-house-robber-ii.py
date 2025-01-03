# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robMoney(money: List[int]):
            dp = [0 for _ in range(len(money) + 1)]
            dp[0] = 0
            dp[1] = money[0]
            for i in range(2, len(money) + 1):
                dp[i] = max(dp[i-2] + money[i-1], dp[i-1])
            return dp[-1]

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(robMoney(nums[:-1]), robMoney(nums[1:]))


nums = [2, 3, 2]
print(Solution().rob(nums))
nums = [1, 2, 3, 1]
print(Solution().rob(nums))
nums = [1, 2, 3]
print(Solution().rob(nums))
