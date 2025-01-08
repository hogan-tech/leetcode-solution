# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
        return count


words = ["a", "aba", "ababa", "aa"]
print(Solution().countPrefixSuffixPairs(words))
words = ["pa", "papa", "ma", "mama"]
print(Solution().countPrefixSuffixPairs(words))
words = ["abab", "ab"]
print(Solution().countPrefixSuffixPairs(words))
