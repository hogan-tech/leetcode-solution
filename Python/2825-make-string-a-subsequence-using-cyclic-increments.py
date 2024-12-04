# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def match(c1: str, c2: str) -> bool:
            c1 = ord(c1) - ord('a')
            c2 = ord(c2) - ord('a')
            return c1 == c2 or (c1 + 1) % 26 == c2
        j = 0
        for c in str1:
            if match(c, str2[j]):
                j += 1
            if j == len(str2):
                return True
        return False


str1 = "abc"
str2 = "ad"
print(Solution().canMakeSubsequence(str1, str2))
str1 = "zc"
str2 = "ad"
print(Solution().canMakeSubsequence(str1, str2))
str1 = "ab"
str2 = "d"
print(Solution().canMakeSubsequence(str1, str2))
