# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def isValid(self, word: str) -> bool:
        vowel = False
        consonant = False
        if len(word) < 3:
            return False
        for c in word:
            if not c.isalnum():
                return False
            if c.isalpha():
                if c in 'aeiouAEIOU':
                    vowel = True
                else:
                    consonant = True
        return vowel and consonant


word = "234Adas"
print(Solution().isValid(word))
word = "b3"
print(Solution().isValid(word))
word = "a3$e"
print(Solution().isValid(word))
