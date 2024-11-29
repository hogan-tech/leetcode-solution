# time complexity: O(n)
# space complexity: O(1)
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1CounterValue = Counter(word1).values()
        word2CounterValue = Counter(word2).values()
        word1CounterKey = Counter(word1).keys()
        word2CounterKey = Counter(word2).keys()

        return sorted(word1CounterValue) == sorted(word2CounterValue) and sorted(word1CounterKey) == sorted(word2CounterKey)


word1 = "cabbba"
word2 = "abbccc"

print(Solution().closeStrings(word1, word2))
