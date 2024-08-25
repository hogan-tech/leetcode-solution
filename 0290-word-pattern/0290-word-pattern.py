class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternMap, wordMap = {}, {}
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        for char, word in zip(pattern, words):
            if char not in patternMap:
                if word in wordMap:
                    return False
                else:
                    patternMap[char] = word
                    wordMap[word] = char
            else:
                if patternMap[char] != word:
                    return False
        return True


pattern = "abba"
s = "dog cat cat dog"
print(Solution().wordPattern(pattern, s))
