class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
                dp[i] += dp[i - 2]
        return dp[n]