# time complexity: O(mn)
# space complexity: O(mn)
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                k = i + j
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[k-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[k-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[k-1]
                                ) or (dp[i][j-1] and s2[j-1] == s3[k-1])
        return dp[-1][-1]

# time complexity: O(mn)
# space complexity: O(mn)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache(None)
        def dp(i: int, j: int) -> bool:
            k = i + j
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            result = False
            if s3[k] == s1[i] and dp(i + 1, j):
                result = True
            elif s3[k] == s2[j] and dp(i, j + 1):
                result = True
            return result

        return dp(0, 0)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(Solution().isInterleave(s1, s2, s3))
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(Solution().isInterleave(s1, s2, s3))
s1 = ""
s2 = ""
s3 = ""
print(Solution().isInterleave(s1, s2, s3))
