# time complexity: O(n*m)
# space compleixty: O(n*m)

# Bottom Up
from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dpGrid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for t2 in reversed(range(len(text2))):
            for t1 in reversed(range(len(text1))):
                if text1[t1] == text2[t2]:
                    dpGrid[t1][t2] = dpGrid[t1+1][t2+1] + 1
                else:
                    dpGrid[t1][t2] = max(
                        dpGrid[t1+1][t2], dpGrid[t1][t2+1])
        return dpGrid[0][0]

# time complexity: O(n*m)
# space compleixty: O(n*m)

# Top Down
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        T1 = len(text1)
        T2 = len(text2)
        dp = [[0 for _ in range(T2 + 1)] for _ in range(T1 + 1)]
        for t1 in range(T1):
            for t2 in range(T2):
                if text1[t1] == text2[t2]:
                    if t1 == 0 and t2 == 0:
                        dp[t1][t2] = 1
                    else:
                        dp[t1][t2] = dp[t1-1][t2-1] + 1
                if t1 > 0 and dp[t1-1][t2] > dp[t1][t2]:
                    dp[t1][t2] = dp[t1-1][t2]
                if t2 > 0 and dp[t1][t2-1] > dp[t1][t2]:
                    dp[t1][t2] = dp[t1][t2-1]
        return dp[T1 - 1][T2 - 1]


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
text1 = "abc"
text2 = "abc"
print(Solution().longestCommonSubsequence(text1, text2))
text1 = "abc"
text2 = "def"
print(Solution().longestCommonSubsequence(text1, text2))