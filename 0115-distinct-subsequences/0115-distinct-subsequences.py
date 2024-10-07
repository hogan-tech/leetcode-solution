# time complexity: O(m*n)
# space complexity: O(m*n)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M = len(s)
        N = len(t)
        dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
        for j in range(N + 1):
            dp[M][j] = 0
        for i in range(M + 1):
            dp[i][N] = 1

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]


s = "rabbbit"
t = "rabbit"
print(Solution().numDistinct(s, t))
