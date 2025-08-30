# time complexity: O(1)
# space complexity: O(1)
from typing import Counter


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = Counter(str(n))
        result = float('inf')
        minFreq = float('inf')
        for key, value in freq.items():
            if value < minFreq:
                minFreq = value
                result = int(key)
            elif value == minFreq:
                minFreq = value
                result = min(result, int(key))
        return result


n = 1553322
print(Solution().getLeastFrequentDigit(n))
n = 723344511
print(Solution().getLeastFrequentDigit(n))
n = 115
print(Solution().getLeastFrequentDigit(n))
