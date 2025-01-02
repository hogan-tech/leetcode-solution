# time complexity: O(n)
# space complexity: O(n)
from functools import lru_cache

# Bottom Up
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 2 or n == 1:
            return 1
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[-1]

# Top Down
class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(None)
        def dp(idx:int):
            if idx == 0:
                return 0
            if idx == 1 or idx == 2:
                return 1
            return dp(idx - 1) + dp(idx - 2) + dp(idx - 3)
        return dp(n)

print(Solution().tribonacci(0))
print(Solution().tribonacci(4))
print(Solution().tribonacci(5))
print(Solution().tribonacci(25))
