from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrFreq = Counter(arr).values()
        return len(set(arrFreq)) == len(list(arrFreq))


arr = [1, 2]
print(Solution().uniqueOccurrences(arr))
