# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        left = 0
        result = 0
        for right in range(len(s)):
            if s[right] == '1':
                result += (right - left + 1)
            else:
                left = right + 1
        return result % MOD


s = "0110111"
print(Solution().numSub(s))
s = "101"
print(Solution().numSub(s))
s = "000"
print(Solution().numSub(s))
s = "111111"
print(Solution().numSub(s))
