# time complexity: O(m*n)
# space complexity: O(m+n)
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowSet, colSet = set(), set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rowSet.add(r)
                    colSet.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rowSet or c in colSet:
                    matrix[r][c] = 0

# time complexity: O(r*c)
# space complexity: O(1)
class Solution(object):
    def setZeroes(self, grid: List[List[int]]) -> None:
        isCol = False
        ROW = len(grid)
        COL = len(grid[0])
        for r in range(ROW):
            if grid[r][0] == 0:
                isCol = True
            for c in range(1, COL):
                if grid[r][c] == 0:
                    grid[0][c] = 0
                    grid[r][0] = 0

        for r in range(1, ROW):
            for c in range(1, COL):
                if not grid[r][0] or not grid[0][c]:
                    grid[r][c] = 0

        if grid[0][0] == 0:
            for c in range(COL):
                grid[0][c] = 0

        if isCol:
            for r in range(ROW):
                grid[r][0] = 0


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(Solution().setZeroes(matrix))
