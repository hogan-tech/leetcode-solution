class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if (i == len(s1)):
                    if (j != len(s2)): dp[i][j] = ord(s2[j]) + dp[i][j + 1]
                    continue
                if (j == len(s2)):
                    if (i != len(s1)): dp[i][j] = ord(s1[i]) + dp[i + 1][j]
                    continue
                if (s1[i] != s2[j]):
                    dp[i][j] = min(ord(s1[i]) + dp[i + 1][j], ord(s2[j]) + dp[i][j + 1])
                else: dp[i][j] = dp[i + 1][j + 1]
        return dp[0][0]