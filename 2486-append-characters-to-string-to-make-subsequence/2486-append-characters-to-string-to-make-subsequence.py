# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        return len(t) - j


s = "coaching"
t = "coding"
print(Solution().appendCharacters(s, t))
