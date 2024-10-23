# time complexity: O(m*n)
# space complexity: O(m*n)
from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        seen = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(currR: int, currC: int):
            queue = deque()
            queue.append([currR, currC])
            seen.add((currR, currC))
            isClosed = True
            while queue:
                currR, currC = queue.popleft()
                if currR == 0 or currR == ROW - 1 or currC == 0 or currC == COL - 1:
                    isClosed = False

                for dirR, dirC in directions:
                    nextR = currR + dirR
                    nextC = currC + dirC
                    if 0 <= nextR < ROW and 0 <= nextC < COL:
                        if (nextR, nextC) not in seen and grid[nextR][nextC] == 0:
                            seen.add((nextR, nextC))
                            queue.append([nextR, nextC])
            return isClosed

        count = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0 and (i, j) not in seen and bfs(i, j):
                    count += 1

        print(seen)
        return count


grid = [[1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]]

print(Solution().closedIsland(grid))
