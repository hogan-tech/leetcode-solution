# time complexity: O(2^w*(L+A))
# space complexity: O(A + W)
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        W = len(words)
        self.maxScore = 0
        freq = [0 for i in range(26)]
        subsetLetters = [0 for i in range(26)]
        for c in letters:
            freq[ord(c) - 97] += 1

        def isValidWord(subsetLetters):
            for c in range(26):
                if freq[c] < subsetLetters[c]:
                    return False
            else:
                return True

        def check(w, words, score, subsetLetters, totalScore):
            if w == -1:
                self.maxScore = max(self.maxScore, totalScore)
                return
            check(w - 1, words, score, subsetLetters, totalScore)
            L = len(words[w])
            for i in range(L):
                c = ord(words[w][i]) - 97
                subsetLetters[c] += 1
                totalScore += score[c]

            if isValidWord(subsetLetters):
                check(w - 1, words, score, subsetLetters, totalScore)

            for i in range(L):
                c = ord(words[w][i]) - 97
                subsetLetters[c] -= 1
                totalScore -= score[c]

        check(W - 1, words, score, subsetLetters, 0)
        return self.maxScore


ords = ["dog", "cat", "dad", "good"]
letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0,
         0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(Solution().maxScoreWords(ords, letters, score))
