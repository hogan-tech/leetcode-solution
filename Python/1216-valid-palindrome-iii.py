class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        N = len(s)
        if N//2 < k:
            return True
        memo = [[0] * N for _ in range(N)]

        def dp(s, i, j):
            if i == j:
                return 0
            if i == j - 1:
                return 1 if s[i] != s[j] else 0
            if memo[i][j]:
                return memo[i][j]
            if s[i] == s[j]:
                memo[i][j] = dp(s, i + 1, j - 1)
                return memo[i][j]
            memo[i][j] = 1 + min(dp(s, i + 1, j), dp(s, i, j - 1))
            return memo[i][j]
        return dp(s, 0, N - 1) <= k


s = "abcdeca"
k = 2
print(Solution().isValidPalindrome(s, k))
