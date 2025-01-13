# time complexity: O(n)
# space complexity: O(n)
from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        freqMap = Counter(s)
        count = 0
        for freq in freqMap.values():
            if freq % 2:
                count += freq - 1
            else:
                count += freq - 2
        return len(s) - count


s = "abaacbcbb"
print(Solution().minimumLength(s))
s = "aa"
print(Solution().minimumLength(s))
