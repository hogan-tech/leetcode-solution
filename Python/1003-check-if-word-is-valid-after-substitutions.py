# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        while "abc" in s:
            s = s.replace('abc', '')
        return len(s) == 0


s = "aabcbc"
print(Solution().isValid(s))
s = "abcabcababcc"
print(Solution().isValid(s))
s = "abccba"
print(Solution().isValid(s))
