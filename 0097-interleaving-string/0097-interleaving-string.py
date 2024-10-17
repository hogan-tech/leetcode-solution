# time complexity: O(mn)
# space complexity: O(mn)
from functools import lru_cache

import numpy as np


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = np.full([len(s1) + 1, len(s2) + 1], False)
        dp[0][0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0 and s1[i-1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1, j]
                if j > 0 and s2[j-1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i, j - 1]
        return dp[len(s1), len(s2)]

# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         m, n, o = len(s1), len(s2), len(s3)
#         if m+n != o:
#             return False
#         dp = [[False] * (n+1) for _ in range(m+1)]
#         for i in range(m+1):
#             for j in range(n+1):
#                 if i == 0 and j == 0:
#                     dp[i][j] = True
#                 elif i == 0:
#                     dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
#                 elif j == 0:
#                     dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
#                 else:
#                     dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]
#                                 ) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
#         return dp[m][n]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(Solution().isInterleave(s1, s2, s3))
