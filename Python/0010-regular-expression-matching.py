# time complexity: O((t + p) * 2 ^ (t + p/2))
# space complexity: O(t^2 + p ^ 2)
from functools import lru_cache


class Solution(object):
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text
        firstMatch = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern) >= 2 and pattern[1] == '*':
            return self.isMatch(text, pattern[2:]) or firstMatch and self.isMatch(text[1:], pattern)
        else:
            return firstMatch and self.isMatch(text[1:], pattern[1:])

# time complexity: O(tp)
# space complexity: O(tp)
class Solution(object):
    def isMatch(self, text: str, pattern: str) -> bool:
        @lru_cache(None)
        def dp(tIdx: int, pIdx: int) -> bool:
            if pIdx == len(pattern):
                result = tIdx == len(text)
            else:
                firstMatch = tIdx < len(text) and pattern[pIdx] in {
                    text[tIdx], "."}
                if pIdx + 1 < len(pattern) and pattern[pIdx + 1] == "*":
                    result = dp(
                        tIdx, pIdx + 2) or firstMatch and dp(tIdx + 1, pIdx)
                else:
                    result = firstMatch and dp(tIdx + 1, pIdx + 1)
            return result
        return dp(0, 0)

# time complexity: O(tp)
# space complexity: O(tp)
class Solution(object):
    def isMatch(self, text: str, pattern: str) -> bool:
        dp = [[False for _ in range(len(pattern) + 1)]
              for _ in range(len(text) + 1)]
        dp[-1][-1] = True
        for tIdx in range(len(text), -1, -1):
            for jIdx in range(len(pattern) - 1, -1, -1):
                firstMatch = tIdx < len(text) and pattern[jIdx] in {text[tIdx], "."}
                if jIdx + 1 < len(pattern) and pattern[jIdx + 1] == "*":
                    dp[tIdx][jIdx] = dp[tIdx][jIdx + 2] or firstMatch and dp[tIdx + 1][jIdx]
                else:
                    dp[tIdx][jIdx] = firstMatch and dp[tIdx + 1][jIdx + 1]

        return dp[0][0]


s = "aa"
p = "a"
print(Solution().isMatch(s, p))
s = "aa"
p = "a*"
print(Solution().isMatch(s, p))
s = "ab"
p = ".*"
print(Solution().isMatch(s, p))
