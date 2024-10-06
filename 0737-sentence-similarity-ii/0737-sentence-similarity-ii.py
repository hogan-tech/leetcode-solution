# time complexity: O((n + k) * m)
# space complexity: O(k*m)
from itertools import chain
from typing import List


class UnionFind:
    def __init__(self, words: set):
        self.parents = {w: w for w in words}
        self.rank = {w: 1 for w in words}

    def find(self, node: str):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, nodeX: str, nodeY: str):
        parentX = self.find(nodeX)
        parentY = self.find(nodeY)

        if parentX == parentY:
            return
        self.parents[parentX] = parentY


class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        words = set(chain(*similarPairs))
        if len(sentence1) != len(sentence2):
            return False

        for word1, word2 in zip(sentence1, sentence2):
            words.add(word1)
            words.add(word2)

        disjointUnionSet = UnionFind(words)

        for startVertex, endVertex in similarPairs:
            disjointUnionSet.union(startVertex, endVertex)

        for word1, word2 in zip(sentence1, sentence2):
            if disjointUnionSet.find(word1) != disjointUnionSet.find(word2):
                return False
        return True


sentence1 = ["great", "acting", "skills"]
sentence2 = ["fine", "drama", "talent"]
similarPairs = [["great", "good"], ["fine", "good"],
                ["drama", "acting"], ["skills", "talent"]]
print(Solution().areSentencesSimilarTwo(sentence1, sentence2, similarPairs))
