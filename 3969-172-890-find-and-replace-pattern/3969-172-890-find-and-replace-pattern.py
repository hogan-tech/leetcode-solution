# time complexity: O(n^2)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            if len(word) != len(pattern):
                break
            patternDict = defaultdict(str)
            wordDict = defaultdict(str)
            match = True
            for i in range(len(pattern)):
                patternC = pattern[i]
                wordC = word[i]
                if patternC not in patternDict:
                    patternDict[patternC] = wordC
                if patternC in patternDict and wordC != patternDict[patternC]:
                    match = False
                    break
                if wordC not in wordDict:
                    wordDict[wordC] = patternC
                if wordC in wordDict and patternC != wordDict[wordC]:
                    match = False
                    break
            if match:
                result.append(word)
        return result


'''
a:c
b:c
b:c

in patternC and wordC != patternDict[]
'''

words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
print(Solution().findAndReplacePattern(words, pattern))
words = ["a", "b", "c"]
pattern = "a"
print(Solution().findAndReplacePattern(words, pattern))
