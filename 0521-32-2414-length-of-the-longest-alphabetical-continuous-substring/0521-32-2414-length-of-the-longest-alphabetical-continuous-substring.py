# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        left = 0
        result = 0
        for right in range(1, len(s)):
            if ord(s[right]) == ord(s[right - 1]) + 1:
                result = max(result, right - left)
            else:
                left = right
        return result + 1


s = "abcabcdefg"
print(Solution().longestContinuousSubstring(s))
s = "abacaba"
print(Solution().longestContinuousSubstring(s))
s = "abcde"
print(Solution().longestContinuousSubstring(s))
