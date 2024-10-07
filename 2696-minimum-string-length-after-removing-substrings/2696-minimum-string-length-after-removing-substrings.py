class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            if "AB" in s:
                s = s.replace("AB", "")
            if "CD" in s:
                s = s.replace("CD", "")
        return len(s)


s = "ABFCACDB"
print(Solution().minLength(s))
