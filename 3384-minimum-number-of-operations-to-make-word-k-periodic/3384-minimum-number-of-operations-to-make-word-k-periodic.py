# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        freq = defaultdict(int)
        freq[word[:k]] += 1
        for i in range(k, len(word), k):
            freq[word[i: i + k]] += 1
        return len(word)//k - max(freq.values())


'''
leetcodeleet
        l
           r

'''
word = "leetcodeleet"
k = 4
print(Solution().minimumOperationsToMakeKPeriodic(word, k))
word = "leetcoleet"
k = 2
print(Solution().minimumOperationsToMakeKPeriodic(word, k))
