# time complexity: O(m*n*log(m*n))
# space complexity: O(log(m*n))
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        visited = set()
        pq = [(grid[0][0], 0, 0)]
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while pq:
            currTime, currR, currC = heappop(pq)
            if currR == ROW - 1 and currC == COL - 1:
                return currTime
            if (currR, currC) in visited:
                continue
            visited.add((currR, currC))
            waitTime = 0
            for dR, dC in DIRS:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL and (nextR, nextC) not in visited:
                    if (grid[nextR][nextC] - currTime) % 2 == 0:
                        waitTime = 1
                    else:
                        waitTime = 0
                    nextTime = max(grid[nextR][nextC] + waitTime, currTime + 1)
                    heappush(pq, (nextTime, nextR, nextC))
        return -1


grid = [[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]
print(Solution().minimumTime(grid))
grid = [[0, 2, 4], [3, 2, 1], [1, 0, 4]]
print(Solution().minimumTime(grid))
