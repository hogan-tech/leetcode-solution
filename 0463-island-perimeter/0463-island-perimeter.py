# time complexity: O(n*m)
# space complexity: O(1)
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        edgeCount = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if (j > 0 and grid[i][j - 1] == 0) or j == 0:
                        edgeCount += 1
                    if (i > 0 and grid[i - 1][j] == 0) or i == 0:
                        edgeCount += 1
                    if (j < col - 1 and grid[i][j + 1] == 0) or j == col - 1:
                        edgeCount += 1
                    if (i < row - 1 and grid[i + 1][j] == 0) or i == row - 1:
                        edgeCount += 1
        return edgeCount


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(Solution().islandPerimeter(grid))
