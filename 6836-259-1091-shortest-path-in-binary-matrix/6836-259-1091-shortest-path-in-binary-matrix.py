# time complexity: O(m*n)
# space complexity: O(m*n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        pq = []
        pq.append((1, (0, 0)))
        if grid[0][0] != 0:
            return -1

        Dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]
        while pq:
            distance, (currR, currC) = heappop(pq)
            grid[currR][currC] = 1
            if currR == ROW - 1 and currC == COL - 1:
                return distance
            for dR, dC in Dirs:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL and grid[nextR][nextC] == 0:
                    heappush(pq, (distance + 1, (nextR, nextC)))
                    grid[nextR][nextC] = 1

        return -1


grid = [[0, 1], [1, 0]]
print(Solution().shortestPathBinaryMatrix(grid))
grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(Solution().shortestPathBinaryMatrix(grid))
grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
print(Solution().shortestPathBinaryMatrix(grid))
