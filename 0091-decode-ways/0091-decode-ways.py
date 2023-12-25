from functools import lru_cache


class Solution:
    @lru_cache(None)
    def recursiveWithMemo(self, index: int, s: str) -> int:
        if index == len(s):
            return 1
        if s[index] == '0':
            return 0
        if index == len(s) - 1:
            return 1
        answer = self.recursiveWithMemo(index + 1, s)
        if int(s[index: index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)
        return answer

    def numDecodings(self, s: str) -> int:
        return self.recursiveWithMemo(0, s)


s = "12"
print(Solution().numDecodings(s))
