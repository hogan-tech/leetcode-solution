# time complexity: O(mn)
# space complexity: O(1)
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        for r in range(1, ROW):
            grid[r][0] += grid[r-1][0]
        for c in range(1, COL):
            grid[0][c] += grid[0][c-1]
        for r in range(1, ROW):
            for c in range(1, COL):
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        return grid[ROW-1][COL-1]

# time complexity: O(mn)
# space complexity: O(mn)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dp = [[0 for _ in range(COL + 1)] for _ in range(ROW + 1)]
        for r in range(1, ROW + 1):
            for c in range(1, COL + 1):
                if c == 1:
                    dp[r][c] = dp[r - 1][c] + grid[r - 1][c - 1]
                elif r == 1:
                    dp[r][c] = dp[r][c - 1] + grid[r - 1][c - 1]
                else:
                    dp[r][c] = min(dp[r][c - 1], dp[r - 1]
                                   [c]) + grid[r - 1][c - 1]
        return dp[ROW][COL]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(Solution().minPathSum(grid))
grid = [[1, 2, 3], [4, 5, 6]]
print(Solution().minPathSum(grid))
