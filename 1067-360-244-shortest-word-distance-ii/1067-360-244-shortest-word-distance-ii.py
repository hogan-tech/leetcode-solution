# time complexity: O(n^2)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsdict = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.wordsdict[word].append(i)
        return

    def shortest(self, word1: str, word2: str) -> int:
        word1Idx = self.wordsdict[word1]
        word2Idx = self.wordsdict[word2]
        minDistance = float('inf')
        for i in range(len(word1Idx)):
            for j in range(len(word2Idx)):
                minDistance = min(minDistance, abs(word1Idx[i] - word2Idx[j]))
        return minDistance


# Your WordDistance object will be instantiated and called as such:
obj = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print(obj.shortest("coding", "practice"))
print(obj.shortest("makes", "coding"))
