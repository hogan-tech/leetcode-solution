from typing import List


class Solution(object):
    def onesMinusZeros(self, grid):
        n = len(grid)
        m = len(grid[0])
        row = [0] * n
        col = [0] * m
        diff = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row[i] += grid[i][j]
                    col[j] += grid[i][j]

        for i in range(n):
            for j in range(m):
                diff[i][j] = (2 * row[i] - n) + (2 * col[j] - m)

        return diff


grid = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
print(Solution().onesMinusZeros(grid))
