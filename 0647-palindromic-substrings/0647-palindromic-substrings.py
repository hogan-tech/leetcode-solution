# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        if n <= 0:
            return 0

        # Initialize 2D list (dp array) with False
        dp = [[False for _ in range(n)] for _ in range(n)]

        # Base case: single letter substrings
        for i in range(n):
            dp[i][i] = True
            ans += 1

        # Base case: double letter substrings
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            ans += dp[i][i + 1]

        # All other cases: substrings of length 3 to n
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                ans += dp[i][j]

        return ans


s = "aaa"
print(Solution().countSubstrings(s))
