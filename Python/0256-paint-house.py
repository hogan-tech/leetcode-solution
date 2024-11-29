from functools import lru_cache
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @lru_cache(None)
        def paintCost(n: int, color: int) -> int:
            totalCost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:
                totalCost += min(paintCost(n+1, 1), paintCost(n+1, 2))
            elif color == 1:
                totalCost += min(paintCost(n+1, 0), paintCost(n+1, 2))
            else:
                totalCost += min(paintCost(n+1, 0), paintCost(n+1, 1))
            return totalCost

        if costs == []:
            return 0
        return min(paintCost(0, 0), paintCost(0, 1), paintCost(0, 2))


costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
print(Solution().minCost(costs))
