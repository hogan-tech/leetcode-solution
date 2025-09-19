# time complexity: O(n)
# space complexity: O(n)
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

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n = len(costs)
        for i in range(1, n):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[-1])

costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
print(Solution().minCost(costs))
costs = [[7, 6, 2]]
print(Solution().minCost(costs))
