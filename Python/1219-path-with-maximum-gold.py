# time complexity: O(m*n*3^g)
# space complexity: O(g)
from typing import List


class Solution:
    rowDir = [1, -1, 0, 0]
    colDir = [0, 0, 1, -1]

    def dfs(self, grid: List[List[int]], x: int, y: int, n: int, m: int):
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
            return 0

        curr = grid[x][y]
        grid[x][y] = 0
        localMaxGold = curr

        for i in range(4):
            newX = x + self.rowDir[i]
            newY = y + self.colDir[i]
            localMaxGold = max(localMaxGold, curr +
                               self.dfs(grid, newX, newY, n, m))

        grid[x][y] = curr
        return localMaxGold

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        maxGold = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    maxGold = max(maxGold, self.dfs(grid, i, j, n, m))
        return maxGold


grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
print(Solution().getMaximumGold(grid))
