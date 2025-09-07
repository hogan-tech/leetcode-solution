# time complexity: O(nlogm)
# space complexity: O(1)
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            target = 0
            for pile in piles:
                target += math.ceil(pile / mid)
            if h < target:
                left = mid + 1
            else:
                right = mid
        return right


piles = [3, 6, 7, 11]
h = 8
print(Solution().minEatingSpeed(piles, h))
piles = [30, 11, 23, 4, 20]
h = 5
print(Solution().minEatingSpeed(piles, h))
piles = [30, 11, 23, 4, 20]
h = 6
print(Solution().minEatingSpeed(piles, h))
