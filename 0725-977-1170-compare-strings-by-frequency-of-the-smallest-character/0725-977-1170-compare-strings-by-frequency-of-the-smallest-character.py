# time complexity: O(nlogn)
# space complexity: O(n)
from bisect import bisect_right
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def convertFreq(s: str):
            alpha = [0] * 26
            for c in s:
                alpha[ord(c) - ord('a')] += 1
            for num in alpha:
                if num != 0:
                    return num
            return 0
        queries = [convertFreq(query) for query in queries]
        words = sorted([convertFreq(word) for word in words])
        result = []
        for query in queries:
            idx = bisect_right(words, query)
            result.append(len(words) - idx)
        return result


queries = ["cbd"]
words = ["zaaaz"]
print(Solution().numSmallerByFrequency(queries, words))
queries = ["bbb", "cc"]
words = ["a", "aa", "aaa", "aaaa"]
print(Solution().numSmallerByFrequency(queries, words))
