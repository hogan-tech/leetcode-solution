# time complexity: O(m*n)
# space complexity: O(m*n)
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         M = len(s)
#         N = len(t)
#         dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
#         for j in range(N + 1):
#             dp[M][j] = 0
#         for i in range(M + 1):
#             dp[i][N] = 1
#         for i in range(M - 1, -1, -1):
#             for j in range(N - 1, -1, -1):
#                 dp[i][j] = dp[i + 1][j]
#                 if s[i] == t[j]:
#                     dp[i][j] += dp[i + 1][j + 1]
#         return dp[0][0]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, m + 1):
                if s[i - 1] != t[j - 1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp[n][m]


s = "rabbbit"
t = "rabbit"
print(Solution().numDistinct(s, t))
