# time complexity: O(n*m)
# space complexity: O(1)
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        edgeCount = 0
        ROW = len(grid)
        COL = len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    if (c > 0 and grid[r][c - 1] == 0) or c == 0:
                        edgeCount += 1
                    if (r > 0 and grid[r - 1][c] == 0) or r == 0:
                        edgeCount += 1
                    if (c < COL - 1 and grid[r][c + 1] == 0) or c == COL - 1:
                        edgeCount += 1
                    if (r < ROW - 1 and grid[r + 1][c] == 0) or r == ROW - 1:
                        edgeCount += 1
        return edgeCount


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(Solution().islandPerimeter(grid))
grid = [[1]]
print(Solution().islandPerimeter(grid))
grid = [[1, 0]]
print(Solution().islandPerimeter(grid))
