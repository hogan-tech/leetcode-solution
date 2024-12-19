# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return checkPalindrome(s, i, j - 1) or checkPalindrome(s, i + 1, j)
            i += 1
            j -= 1

        return True


s = "aba"
print(Solution().validPalindrome(s))
s = "abca"
print(Solution().validPalindrome(s))
s = "abc"
print(Solution().validPalindrome(s))
