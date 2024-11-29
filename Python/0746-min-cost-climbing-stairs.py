from functools import lru_cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache
        def minCost(i):
            if i <= 1:
                return 0
            downOne = cost[i-1] + minCost(i-1)
            downTwo = cost[i-2] + minCost(i-2)
            return min(downOne, downTwo)
        return minCost(len(cost))


cost = [10, 15, 20]
print(Solution().minCostClimbingStairs(cost))
