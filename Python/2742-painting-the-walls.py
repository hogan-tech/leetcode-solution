from cmath import inf
from functools import lru_cache
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        prevDp = [inf] * (n + 1)
        prevDp[0] = 0

        for i in range(n - 1, -1, -1):
            dp = [0] * (n + 1)
            for remain in range(1, n + 1):
                paint = cost[i] + prevDp[max(0, remain - 1 - time[i])]
                dontPaint = prevDp[remain]
                dp[remain] = min(paint, dontPaint)

            prevDp = dp

        return dp[n]


cost = [1, 2, 3, 2]
time = [1, 2, 3, 2]


print(Solution().paintWalls(cost, time))
