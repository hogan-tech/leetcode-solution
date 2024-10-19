# time complexity: O(n*m)
# space complexity: O(n*m)
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i-1] == str2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        result = ""
        i, j = n, m
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result += str1[i-1]
                i, j = i-1, j - 1
            elif dp[i-1][j] > dp[i][j-1]:
                result += str1[i-1]
                i = i-1
            else:
                result += str2[j-1]
                j = j-1

        result = result[::-1]

        return str1[:i] + str2[:j]+result


str1 = "abac"
str2 = "cab"
print(Solution().shortestCommonSupersequence(str1, str2))
