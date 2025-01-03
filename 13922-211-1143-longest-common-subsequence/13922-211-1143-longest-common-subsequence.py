# time complexity: O(n*m)
# space compleixty: O(n*m)

# Bottom Up
from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dpGrid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text1[row] == text2[col]:
                    dpGrid[row][col] = dpGrid[row+1][col+1] + 1
                else:
                    dpGrid[row][col] = max(
                        dpGrid[row+1][col], dpGrid[row][col+1])
        return dpGrid[0][0]

# time complexity: O(n*m)
# space compleixty: O(n*m)

# Top Down
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROW = len(text1)
        COL = len(text2)
        dp = [[0 for _ in range(COL + 1)] for _ in range(ROW + 1)]
        for r in range(ROW):
            for c in range(COL):
                if text1[r] == text2[c]:
                    if r == 0 and c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = dp[r-1][c-1] + 1
                if r > 0 and dp[r-1][c] > dp[r][c]:
                    dp[r][c] = dp[r-1][c]
                if c > 0 and dp[r][c-1] > dp[r][c]:
                    dp[r][c] = dp[r][c-1]
        return dp[ROW - 1][COL - 1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dp(p1: int, p2: int):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if text1[p1] == text2[p2]:
                return 1 + dp(p1 + 1, p2 + 1)
            else:
                return max(dp(p1, p2 + 1), dp(p1 + 1, p2))
        return dp(0, 0)


text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2))
