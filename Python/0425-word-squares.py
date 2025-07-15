# time complexity: O(n*26^l)
# space complexity: O(n*l)
from collections import defaultdict
from typing import List


class Solution:

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        N = len(words[0])
        prefixHashTable = defaultdict(set)
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                prefixHashTable[prefix].add(word)

        def getWordsWithPrefix(prefix):
            if prefix in prefixHashTable:
                return prefixHashTable[prefix]
            else:
                return set([])

        def backtracking(step, wordSquares, results):
            if step == N:
                results.append(wordSquares[:])
                return

            prefix = ''.join([word[step] for word in wordSquares])
            for candidate in getWordsWithPrefix(prefix):
                wordSquares.append(candidate)
                backtracking(step+1, wordSquares, results)
                wordSquares.pop()

        results = []
        wordSquares = []
        for word in words:
            wordSquares = [word]
            backtracking(1, wordSquares, results)
        return results


words = ["area", "lead", "wall", "lady", "ball"]
print(Solution().wordSquares(words))
words = ["abat", "baba", "atan", "atal"]
print(Solution().wordSquares(words))
