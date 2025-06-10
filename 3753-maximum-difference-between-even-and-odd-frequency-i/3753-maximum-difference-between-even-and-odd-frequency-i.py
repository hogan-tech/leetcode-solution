# time complexity: O(n)
# space complexity: O(n)
from typing import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        oddCount = float('-inf')
        evenCount = float('inf')
        for value in Counter(s).values():
            if value % 2:
                oddCount = max(oddCount, value)
            else:
                evenCount = min(evenCount, value)

        return oddCount - evenCount


s = "aaaaabbc"
print(Solution().maxDifference(s))
s = "abcabcab"
print(Solution().maxDifference(s))
