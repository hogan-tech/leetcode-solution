from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = ['a', 'e', 'i', 'o', 'u']
        isVowels = [0] * n
        result = []
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                isVowels[i] += 1
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] += isVowels[i] + prefixSum[i] 
        for start, end in queries:
            result.append(prefixSum[end + 1] - prefixSum[start])
        return result


words = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0, 2], [1, 4], [1, 1]]
print(Solution().vowelStrings(words, queries))
words = ["a", "e", "i"]
queries = [[0, 2], [0, 1], [2, 2]]
print(Solution().vowelStrings(words, queries))
