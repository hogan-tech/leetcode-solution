# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for left in range(n - 1, -1, -1):
            dp[left][left] = 1
            for right in range(left + 1, n):
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1] + 2
                else:
                    dp[left][right] = max(
                        dp[left + 1][right], dp[left][right - 1])
        return dp[0][n-1]

# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            next = [0] * (m + 1)
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    next[j] = dp[j - 1] + 1
                else:
                    next[j] = max(dp[j], next[j - 1])
            dp = next
        return dp[m]

    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        return self.longestCommonSubsequence(s, t)


s = "bbbab"
print(Solution().longestPalindromeSubseq(s))
s = "cbbd"
print(Solution().longestPalindromeSubseq(s))
