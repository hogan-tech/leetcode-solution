# time complexity: O(n + c^2) = O(n)
# space complexity: O(1)
from typing import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqList = [val for val in Counter(word).values()]
        result = float('inf')
        for freq1 in freqList:
            count = 0
            for freq2 in freqList:
                if freq1 > freq2:
                    count += freq2
                elif freq1 + k < freq2:
                    count += freq2 - (freq1 + k)
            result = min(result, count)
        return result


word = "aabcaba"
k = 0
print(Solution().minimumDeletions(word, k))
word = "dabdcbdcdcd"
k = 2
print(Solution().minimumDeletions(word, k))
word = "aaabaaa"
k = 2
print(Solution().minimumDeletions(word, k))
