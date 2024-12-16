# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robMoney(nums: List[int], start: int, end: int) -> int:
            dp = [0] * (end - start)
            dp[0] = nums[start]
            dp[1] = max(dp[0], nums[start + 1])
            for i in range(start + 2, end):
                dp[i-start] = max(nums[i] + dp[i-start - 2], dp[i-start - 1])

            return dp[-1]

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        money1 = robMoney(nums, 0, n - 1)
        money2 = robMoney(nums, 1, n)

        return max(money1, money2)


nums = [2, 3, 2]
print(Solution().rob(nums))
nums = [1, 2, 3, 1]
print(Solution().rob(nums))
nums = [1, 2, 3]
print(Solution().rob(nums))
