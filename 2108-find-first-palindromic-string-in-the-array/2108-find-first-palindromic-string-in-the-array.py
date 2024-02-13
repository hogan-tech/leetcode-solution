from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isValidPalindrome(s: str) -> bool:
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        for word in words:
            if isValidPalindrome(word):
                return word
        return ""


words = ["notapalindrome","racecar"]
print(Solution().firstPalindrome(words))
