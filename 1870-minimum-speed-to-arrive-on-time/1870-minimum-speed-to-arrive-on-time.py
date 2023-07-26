import math
from typing import List


class Solution:

    def timeRequired(self, dist: List[int], speed: int) -> float:
        time = 0.0
        for i in range(len(dist)):
            t = dist[i]/speed
            time += t if i == len(dist)-1 else math.ceil(t)
        return time

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 1
        right = 10**7
        minSpeed = -1
        while left <= right:
            mid = (right + left) // 2
            if self.timeRequired(dist, mid) <= hour:
                minSpeed = mid
                right = mid - 1
            else:
                left = mid + 1

        return minSpeed