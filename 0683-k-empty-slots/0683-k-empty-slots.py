# time complexity: O(n^2)
# space complexity: O(n)
import bisect
from typing import List


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        active = []
        for day, bulb in enumerate(bulbs, 1):
            i = bisect.bisect(active, bulb)
            for neighbor in active[i-(i > 0):i+1]:
                if abs(neighbor - bulb) - 1 == k:
                    return day
            active.insert(i, bulb)
        return -1


bulbs = [1, 3, 2]
k = 1
print(Solution().kEmptySlots(bulbs, k))
bulbs = [1, 2, 3]
k = 1
print(Solution().kEmptySlots(bulbs, k))
