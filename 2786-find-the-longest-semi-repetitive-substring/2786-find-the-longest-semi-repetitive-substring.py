# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        result = 1
        pair = left = 0
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                pair += 1

            while pair > 1 and left < right:
                if s[left] == s[left + 1]:
                    pair -= 1
                left += 1

            result = max(result, right - left + 1)

        return result


s = "52233"
print(Solution().longestSemiRepetitiveSubstring(s))
s = "5494"
print(Solution().longestSemiRepetitiveSubstring(s))
s = "1111111"
print(Solution().longestSemiRepetitiveSubstring(s))
