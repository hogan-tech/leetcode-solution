class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, (len(s)//2)+1):
            if (len(s) % i == 0):
                subString = s[:i] * (len(s)//i)
                if (s == subString):
                    return True
        return False


s = "abab"

print(Solution().repeatedSubstringPattern(s))
