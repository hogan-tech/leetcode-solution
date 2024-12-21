# time complexity: O(n*m)
# space complexity: O(n*m)
from typing import List


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        ROW = len(grid)
        COL = len(grid[0])
        memo = {}

        def dfs(row: int, col: int, xorValue: int):
            if row >= ROW or col >= COL:
                return 0
            xorValue ^= grid[row][col]

            if row == ROW - 1 and col == COL - 1:
                return 1 if xorValue == k else 0

            if (row, col, xorValue) in memo:
                return memo[(row, col, xorValue)]

            down = dfs(row+1, col, xorValue)
            right = dfs(row, col+1, xorValue)

            memo[(row, col, xorValue)] = (right + down) % MOD
            return memo[(row, col, xorValue)]
        return dfs(0, 0, 0)


grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]]
k = 11
print(Solution().countPathsWithXorValue(grid, k))
grid = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]]
k = 2
print(Solution().countPathsWithXorValue(grid, k))
grid = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]]
k = 10
print(Solution().countPathsWithXorValue(grid, k))
