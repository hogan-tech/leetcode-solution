from collections import defaultdict
from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        wordMap = defaultdict(set)


        for similarPair in similarPairs:
            wordMap[similarPair[0]].add(similarPair[1])
            wordMap[similarPair[1]].add(similarPair[0])

        print(wordMap)
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence2[i] in wordMap[sentence1[i]]:
                continue
            return False
        return True


sentence1 = ["great"]
sentence2 = ["doubleplus", "good"]
similarPairs = [["great", "doubleplus"]]
print(Solution().areSentencesSimilar(sentence1, sentence2, similarPairs))
