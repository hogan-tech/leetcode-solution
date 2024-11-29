# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n-1]


# class Solution:
#     def longestCommonSubsequence(self, s: str, t: str) -> int:
#         n, m = len(s), len(t)
#         dp = [0] * (m + 1)
#         for i in range(1, n + 1):
#             nxt = [0] * (m + 1)
#             for j in range(1, m + 1):
#                 if s[i - 1] == t[j - 1]:
#                     nxt[j] = dp[j - 1] + 1
#                 else:
#                     nxt[j] = max(dp[j], nxt[j - 1])
#             dp = nxt
#         return dp[m]
#     def longestPalindromeSubseq(self, s: str) -> int:
#         t = s[::-1]
#         return self.longestCommonSubsequence(s, t)


s = "bbbab"
print(Solution().longestPalindromeSubseq(s))
