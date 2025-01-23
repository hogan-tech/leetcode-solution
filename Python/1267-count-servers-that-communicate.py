# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        rowCount = [0] * ROW
        colCount = [0] * COL
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    rowCount[r] += 1
                    colCount[c] += 1

        result = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    if rowCount[r] > 1 or colCount[c] > 1:
                        result += 1
        return result


grid = [[1, 0], [0, 1]]
print(Solution().countServers(grid))
grid = [[1, 0], [1, 1]]
print(Solution().countServers(grid))
