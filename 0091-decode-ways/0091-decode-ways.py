# time complexity: O(n)
# space complexity: O(n)
from functools import lru_cache

# Top Down
class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def dp(idx: int) -> int:
            if idx == len(s):
                return 1
            if s[idx] == '0':
                return 0
            if idx == len(s) - 1:
                return 1
            result = dp(idx + 1)
            if int(s[idx: idx + 2]) <= 26:
                result += dp(idx + 2)
            return result
        
        return dp(0)

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i - 1]
            if s[i-2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
                dp[i] += dp[i - 2]

        return dp[n]

s = "12"
print(Solution().numDecodings(s))
s = "226"
print(Solution().numDecodings(s))
s = "06"
print(Solution().numDecodings(s))
