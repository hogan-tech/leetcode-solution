class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        def checkValid(s):
            flag = False
            prev = s[0]
            for i in range(1, len(s)):
                if prev == s[i]:
                    if flag:
                        return False
                    else:
                        flag = True
                prev = s[i]
            return True
            
        result = 0
        for left in range(len(s)):
            for right in range(left, len(s)):
                if checkValid(s[left:right + 1]):
                    result = max(result, right - left + 1)
        return result


s = "52233"
print(Solution().longestSemiRepetitiveSubstring(s))
s = "5494"
print(Solution().longestSemiRepetitiveSubstring(s))
s = "1111111"
print(Solution().longestSemiRepetitiveSubstring(s))