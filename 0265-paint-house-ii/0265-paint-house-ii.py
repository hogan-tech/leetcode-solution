# time complexity: O(n*k^2)
# space complexity: O(1)
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        colorSize = len(costs[0])
        for house in range(1, n):
            for color in range(colorSize):
                best = float("inf")
                for previousColor in range(colorSize):
                    if color == previousColor:
                        continue
                    best = min(best, costs[house - 1][previousColor])
                costs[house][color] += best
        return min(costs[-1])


costs = [[1, 5, 3], [2, 9, 4]]
print(Solution().minCostII(costs))

costs = [[1, 3], [2, 4]]
print(Solution().minCostII(costs))
