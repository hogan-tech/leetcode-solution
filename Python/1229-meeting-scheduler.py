# time complexity: O(mlogm + nlogn)
# space complexity: O(m+n)
from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        idx1, idx2 = 0, 0
        while idx1 < len(slots1) and idx2 < len(slots2):
            left = max(slots1[idx1][0], slots2[idx2][0])
            right = min(slots1[idx1][1], slots2[idx2][1])
            if right - left >= duration:
                return [left, left + duration]
            if slots1[idx1][1] < slots2[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1
        return []


slots1 = [[10, 50], [60, 120], [140, 210]]
slots2 = [[0, 15], [60, 70]]
duration = 8
print(Solution().minAvailableDuration(slots1, slots2, duration))
