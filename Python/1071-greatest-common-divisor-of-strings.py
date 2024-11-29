import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        maxLen = math.gcd(len(str1), len(str2))
        return str1[:maxLen]


str1 = "ABCABC"
str2 = "ABC"

print(Solution().gcdOfStrings(str1, str2))
