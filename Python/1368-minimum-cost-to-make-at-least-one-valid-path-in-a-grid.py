# time complexity: O(n*m*logn*m)
# space complexity: O(n*m)
import heapq
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        pq = [(0, 0, 0)]
        minCost = [[float("inf")] * COL for _ in range(ROW)]
        minCost[0][0] = 0

        while pq:
            cost, currR, currC = heapq.heappop(pq)

            if minCost[currR][currC] != cost:
                continue

            for d, (dR, dC) in enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)]):
                nextR, nextC = currR + dR, currC + dC

                if 0 <= nextR < ROW and 0 <= nextC < COL:
                    nextCost = cost + (d != (grid[currR][currC] - 1))

                    if minCost[nextR][nextC] > nextCost:
                        minCost[nextR][nextC] = nextCost
                        heapq.heappush(pq, (nextCost, nextR, nextC))

        return minCost[ROW - 1][COL - 1]


grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
print(Solution().minCost(grid))
grid = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
print(Solution().minCost(grid))
grid = [[1, 2], [4, 3]]
print(Solution().minCost(grid))
