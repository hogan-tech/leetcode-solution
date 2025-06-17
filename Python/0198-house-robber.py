# time complexity: O(n)
# space complexity: O(n)
from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def robFrom(i):
            if i >= len(nums):
                return 0
            return max(robFrom(i+1), robFrom(i+2) + nums[i])
        return robFrom(0)


nums = [1, 2, 3, 1]
print(Solution().rob(nums))
nums = [2, 7, 9, 3, 1]
print(Solution().rob(nums))
