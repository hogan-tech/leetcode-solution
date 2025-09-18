# time complexity: O(m*n)
# space complexity: O(m*n)
from functools import lru_cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sLen = len(s)
        tLen = len(t)
        dp = [[0 for _ in range(tLen + 1)] for _ in range(sLen + 1)]
        for sIdx in range(sLen + 1):
            dp[sIdx][0] = 1
        for sIdx in range(1, sLen + 1):
            for tIdx in range(1, tLen + 1):
                dp[sIdx][tIdx] = dp[sIdx - 1][tIdx]
                if s[sIdx - 1] == t[tIdx - 1]:
                    dp[sIdx][tIdx] += dp[sIdx - 1][tIdx - 1]
        return dp[sLen][tLen]
    
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def uniqueSubsequences(sIdx: int, tIdx: int) -> int:
            sLen, tLen = len(s), len(t)
            if sIdx == sLen or tIdx == tLen or sLen - sIdx < tLen - tIdx:
                return int(tIdx == len(t))
            result = uniqueSubsequences(sIdx + 1, tIdx)
            if s[sIdx] == t[tIdx]:
                result += uniqueSubsequences(sIdx + 1, tIdx + 1)
            return result
        return uniqueSubsequences(0, 0)

'''
T
    r a b b b i t     S
r                 1 
a                 1
b                 1
b       V         1
i       V V       1
t                 1
    0 0 0 0 0 0 0 
'''

s = "rabbbit"
t = "rabbit"
print(Solution().numDistinct(s, t))
s = "babgbag"
t = "bag"
print(Solution().numDistinct(s, t))
