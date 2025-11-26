# time complexity: O(m * n * k)
# space complexity: O(m * n * k)
from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        ROW, COL = len(grid), len(grid[0])

        dp = [[[0] * k for _ in range(COL + 1)] for _ in range(ROW + 1)]

        for r in range(1, ROW + 1):
            for c in range(1, COL + 1):
                if r == 1 and c == 1:
                    dp[r][c][grid[0][0] % k] = 1
                    continue

                value = grid[r - 1][c - 1] % k
                for i in range(k):
                    prevMod = (i - value + k) % k
                    dp[r][c][i] = (
                        dp[r - 1][c][prevMod] + dp[r][c - 1][prevMod]
                    ) % MOD

        return dp[ROW][COL][0]


grid = [[5, 2, 4], [3, 0, 5], [0, 7, 2]]
k = 3
print(Solution().numberOfPaths(grid, k))
grid = [[0, 0]]
k = 5
print(Solution().numberOfPaths(grid, k))
grid = [[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]]
k = 1
print(Solution().numberOfPaths(grid, k))
