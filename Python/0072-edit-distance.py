# time complexity: O(m*n)
# space complexity: O(m*n)
from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(None)
        def minDisCal(w1: str, w2: str, w1Idx: int, w2Idx: int):
            if w1Idx == 0:
                return w2Idx
            if w2Idx == 0:
                return w1Idx
            minEditDis = 0
            if w1[w1Idx - 1] == w2[w2Idx - 1]:
                minEditDis = minDisCal(w1, w2, w1Idx - 1, w2Idx - 1)
            else:
                insert = minDisCal(w1, w2, w1Idx, w2Idx - 1)
                delete = minDisCal(w1, w2, w1Idx - 1, w2Idx)
                replace = minDisCal(w1, w2, w1Idx - 1, w2Idx - 1)
                minEditDis = (min(insert, delete, replace) + 1)
            return minEditDis
        return minDisCal(word1, word2, len(word1), len(word2))


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        W1, W2 = len(word1), len(word2)
        dp = [[w2 for w2 in range(w1, w1 + W2 + 1)] for w1 in range(W1 + 1)]
        for w1 in range(1, W1 + 1):
            for w2 in range(1, W2 + 1):
                if word1[w1 - 1] == word2[w2 - 1]:
                    dp[w1][w2] = dp[w1-1][w2-1]
                else:
                    dp[w1][w2] = min(dp[w1-1][w2], dp[w1]
                                     [w2-1], dp[w1-1][w2-1]) + 1
        return dp[W1][W2]
'''
a  b  c
   <- w1    
a  b  e
   <- w2

'''

word1 = "horse"
word2 = "ros"
print(Solution().minDistance(word1, word2))
word1 = "intention"
word2 = "execution"
print(Solution().minDistance(word1, word2))
