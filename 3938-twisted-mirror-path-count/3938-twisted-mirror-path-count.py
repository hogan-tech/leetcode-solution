# time complexity: O(r * c)
# space complexity: O(r * c)
from typing import List
from functools import lru_cache

MOD = 10**9 + 7


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        def reflect(r, c, direction):
            while 0 <= r < ROW and 0 <= c < COL and grid[r][c] == 1:
                if direction == 'right':
                    r += 1
                    direction = 'down'
                else:
                    c += 1
                    direction = 'right'
            return (r, c)

        @lru_cache(None)
        def dp(r, c):
            if not (0 <= r < ROW and 0 <= c < COL):
                return 0
            if grid[r][c] == 1:
                return 0
            if (r, c) == (ROW - 1, COL - 1):
                return 1

            total = 0

            nR, nC = r, c + 1
            if 0 <= nC < COL:
                if grid[nR][nC] == 0:
                    total += dp(nR, nC)
                else:
                    reflectR, reflectC = reflect(nR + 1, nC, 'down')
                    if 0 <= reflectR < ROW and 0 <= reflectC < COL and grid[reflectR][reflectC] == 0:
                        total += dp(reflectR, reflectC)

            nR, nC = r + 1, c
            if 0 <= nR < ROW:
                if grid[nR][nC] == 0:
                    total += dp(nR, nC)
                else:
                    reflectR, reflectC = reflect(nR, nC + 1, 'right')
                    if 0 <= reflectR < ROW and 0 <= reflectC < COL and grid[reflectR][reflectC] == 0:
                        total += dp(reflectR, reflectC)

            return total % MOD

        return dp(0, 0)


grid = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
print(Solution().uniquePaths(grid))
grid = [[0, 0], [0, 0]]
print(Solution().uniquePaths(grid))
grid = [[0, 1, 1], [1, 1, 0]]
print(Solution().uniquePaths(grid))
