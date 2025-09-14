# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = set(wordlist)
        caseMap = {}
        vowelMap = {}

        for word in wordlist:
            lower = word.lower()
            devowel = self.deVowel(lower)
            if lower not in caseMap:
                caseMap[lower] = word
            if devowel not in vowelMap:
                vowelMap[devowel] = word

        result = []
        for query in queries:
            if query in exact:
                result.append(query)
            else:
                lower = query.lower()
                devowel = self.deVowel(lower)
                if lower in caseMap:
                    result.append(caseMap[lower])
                elif devowel in vowelMap:
                    result.append(vowelMap[devowel])
                else:
                    result.append("")
        return result

    def deVowel(self, s):
        return ''.join('*' if c in 'aeiou' else c for c in s)


wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = ["kite", "Kite", "KiTe", "Hare", "HARE",
           "Hear", "hear", "keti", "keet", "keto"]
print(Solution().spellchecker(wordlist, queries))
wordlist = ["yellow"]
queries = ["YellOw"]
print(Solution().spellchecker(wordlist, queries))
