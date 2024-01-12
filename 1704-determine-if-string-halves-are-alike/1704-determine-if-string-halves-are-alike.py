class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowelsSet = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        halfCount = 0
        fullCount = 0
        for i in range(len(s)):
            if s[i] in vowelsSet:
                if i < len(s)//2:
                    halfCount += 1
                fullCount += 1
        return halfCount * 2 == fullCount


s = "textbook"
print(Solution().halvesAreAlike(s))
