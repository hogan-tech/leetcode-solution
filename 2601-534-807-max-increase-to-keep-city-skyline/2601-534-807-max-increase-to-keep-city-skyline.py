# time complexity: O(n*m)
# space complexity: O(n*m)
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowList = [max(row) for row in grid]
        colList = []
        result = 0
        ROW = len(grid)
        COL = len(grid[0])
        for c in range(COL):
            tempCOl = 0
            for r in range(ROW):
                tempCOl = max(tempCOl, grid[r][c])
            colList.append(tempCOl)
        for r in range(ROW):
            for c in range(COL):
                result += min(rowList[r], colList[c]) - grid[r][c]

        return result


grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
print(Solution().maxIncreaseKeepingSkyline(grid))
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(Solution().maxIncreaseKeepingSkyline(grid))
