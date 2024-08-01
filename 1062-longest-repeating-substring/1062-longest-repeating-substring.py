# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        maxLength = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    maxLength = max(maxLength, dp[i][j])
        return maxLength


s = "abbaba"
print(Solution().longestRepeatingSubstring(s))
