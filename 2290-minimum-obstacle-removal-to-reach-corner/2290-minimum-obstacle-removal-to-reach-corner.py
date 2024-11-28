# time complexity: O(m*n*log(mn))
# space complexity: O(m*n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        Dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        obsticleGird = [[float('inf')] * COL for _ in range(ROW)]
        obsticleGird[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]

        while pq:
            currObsticle, currR, currC = heappop(pq)
            if currR == ROW - 1 and currC == COL - 1:
                return currObsticle
            for dR, dC in Dirs:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL:
                    nextObsticle = currObsticle + grid[nextR][nextC]
                    if nextObsticle < obsticleGird[nextR][nextC]:
                        obsticleGird[nextR][nextC] = nextObsticle
                        heappush(pq, (nextObsticle, nextR, nextC))

        return obsticleGird[ROW - 1][COL-1]


grid = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
print(Solution().minimumObstacles(grid))
grid = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]
print(Solution().minimumObstacles(grid))
