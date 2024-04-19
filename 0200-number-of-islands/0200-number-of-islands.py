# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        nR = len(grid)
        nC = len(grid[0])
        grid[r][c] = '0'
        if r - 1 >= 0 and grid[r - 1][c] == "1":
            self.dfs(grid, r - 1, c)
        if r + 1 < nR and grid[r + 1][c] == "1":
            self.dfs(grid, r + 1, c)
        if c - 1 >= 0 and grid[r][c - 1] == "1":
            self.dfs(grid, r, c - 1)
        if c + 1 < nC and grid[r][c + 1] == "1":
            self.dfs(grid, r, c + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        numIslands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    numIslands += 1
                    self.dfs(grid, r, c)
        return numIslands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(Solution().numIslands(grid))
