# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        return haystack.index(needle)


haystack = "sabdbutsad"
needle = "sad"
print(Solution().strStr(haystack, needle))
