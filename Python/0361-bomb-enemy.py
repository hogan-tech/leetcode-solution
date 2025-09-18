# time complexity: O(r*c)
# space complexity: O(c)
from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        maxCount = 0
        rowHits = 0
        colHits = [0 for _ in range(COL)]
        for r in range(ROW):
            for c in range(COL):
                if c == 0 or grid[r][c - 1] == 'W':
                    rowHits = 0
                    for i in range(c, COL):
                        if grid[r][i] == 'W':
                            break
                        elif grid[r][i] == 'E':
                            rowHits += 1
                if r == 0 or grid[r - 1][c] == 'W':
                    colHits[c] = 0
                    for i in range(r, ROW):
                        if grid[i][c] == 'W':
                            break
                        elif grid[i][c] == 'E':
                            colHits[c] += 1
                if grid[r][c] == '0':
                    totalHits = rowHits + colHits[c]
                    maxCount = max(maxCount, totalHits)
        return maxCount


grid = [["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]
print(Solution().maxKilledEnemies(grid))
grid = [["W", "W", "W"], ["0", "0", "0"], ["E", "E", "E"]]
print(Solution().maxKilledEnemies(grid))
