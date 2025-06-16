# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]


class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.robFrom(0, nums)

    def robFrom(self, i, nums):

        if i >= len(nums):
            return 0

        if i in self.memo:
            return self.memo[i]

        self.memo[i] = max(self.robFrom(i+1, nums),
                           self.robFrom(i+2, nums) + nums[i])
        return self.memo[i]


nums = [1, 2, 3, 1]
print(Solution().rob(nums))
