# time complexity: O(m*n)
# space complexity: O(1)
from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        rowDiff = 0
        for r in range(ROW):
            for c in range(COL // 2):
                if grid[r][c] != grid[r][COL - c - 1]:
                    rowDiff += 1
        colDiff = 0
        for c in range(COL):
            for r in range(ROW // 2):
                if grid[r][c] != grid[ROW - r - 1][c]:
                    colDiff += 1
        return min(rowDiff, colDiff)


grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
print(Solution().minFlips(grid))
grid = [[0, 1], [0, 1], [0, 0]]
print(Solution().minFlips(grid))
grid = [[1], [0]]
print(Solution().minFlips(grid))
