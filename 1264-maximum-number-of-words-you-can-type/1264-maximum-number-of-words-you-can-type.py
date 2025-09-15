class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetterSet = set([c for c in brokenLetters])
        count = 0
        for word in text.split(' '):
            wordSet = set(word)
            if not (wordSet & brokenLetterSet):
                count += 1
        return count


text = "hello world"
brokenLetters = "ad"
print(Solution().canBeTypedWords(text, brokenLetters))
text = "leet code"
brokenLetters = "lt"
print(Solution().canBeTypedWords(text, brokenLetters))
text = "leet code"
brokenLetters = "e"
print(Solution().canBeTypedWords(text, brokenLetters))
