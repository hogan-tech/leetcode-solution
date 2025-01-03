# time complexity: O(n)
# space complexity: O(n)
from functools import lru_cache

# Top Down
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
    
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        if s[0] == '0':
            return 0
        else:
            dp[1] = 1

        for i in range(2, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <= '6'):
                dp[i] += dp[i-2]

        return dp[n]

s = "12"
print(Solution().numDecodings(s))
s = "226"
print(Solution().numDecodings(s))
s = "06"
print(Solution().numDecodings(s))
