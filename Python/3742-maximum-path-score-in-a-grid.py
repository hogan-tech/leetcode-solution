# time complexity: O(m*n*k)
# space complexity: O(m*n*k)
from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        ROW, COL = len(grid), len(grid[0])

        dp = [[[-10**9 for _ in range(k + 1)]
               for _ in range(COL)] for _ in range(ROW)]

        startVal = grid[0][0]
        startCost = 1 if startVal in (1, 2) else 0
        if startCost <= k:
            dp[0][0][startCost] = startVal

        for r in range(ROW):
            for c in range(COL):
                for i in range(k + 1):
                    if dp[r][c][i] < 0:
                        continue
                    if c + 1 < COL:
                        val = grid[r][c + 1]
                        newCost = i + (1 if val in (1, 2) else 0)
                        if newCost <= k:
                            dp[r][c + 1][newCost] = max(dp[r]
                                                        [c + 1][newCost], dp[r][c][i] + val)
                    if r + 1 < ROW:
                        val = grid[r + 1][c]
                        newCost = i + (1 if val in (1, 2) else 0)
                        if newCost <= k:
                            dp[r + 1][c][newCost] = max(dp[r + 1]
                                                        [c][newCost], dp[r][c][i] + val)

        result = -1
        for i in range(k + 1):
            if dp[ROW - 1][COL - 1][i] >= 0:
                result = max(result, dp[ROW - 1][COL - 1][i])

        return result if result >= 0 else -1


grid = [[0, 1], [2, 0]]
k = 1
print(Solution().maxPathScore(grid, k))
grid = [[0, 1], [1, 2]]
k = 1
print(Solution().maxPathScore(grid, k))
