import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            hourSpent = 0
            for pile in piles:
                hourSpent += math.ceil(pile / mid)
            if hourSpent <= h:
                right = mid
            else:
                left = mid + 1
        return right


piles = [3, 6, 7, 11]
h = 8

print(Solution().minEatingSpeed(piles, h))
