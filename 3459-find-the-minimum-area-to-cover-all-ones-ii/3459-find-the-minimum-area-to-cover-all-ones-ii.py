# time complexity: O(n^2 * m^2)
# space complexity: O(n * m)
import sys
from typing import List


class Solution:
    def minimumSum2(
        self, grid: List[List[int]], u: int, d: int, l: int, r: int
    ) -> int:
        minI = len(grid)
        maxI = 0
        minJ = len(grid[0])
        maxJ = 0

        for i in range(u, d + 1):
            for j in range(l, r + 1):
                if grid[i][j] == 1:
                    minI = min(minI, i)
                    minJ = min(minJ, j)
                    maxI = max(maxI, i)
                    maxJ = max(maxJ, j)

        return (
            (maxI - minI + 1) * (maxJ - minJ + 1)
            if minI <= maxI
            else sys.maxsize // 3
        )

    def rotate(self, vec: List[List[int]]) -> List[List[int]]:
        n = len(vec)
        m = len(vec[0]) if n > 0 else 0
        ret = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                ret[m - j - 1][i] = vec[i][j]

        return ret

    def solve(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        result = n * m

        for i in range(n - 1):
            for j in range(m - 1):
                result = min(
                    result,
                    self.minimumSum2(grid, 0, i, 0, m - 1)
                    + self.minimumSum2(grid, i + 1, n - 1, 0, j)
                    + self.minimumSum2(grid, i + 1, n - 1, j + 1, m - 1),
                )

                result = min(
                    result,
                    self.minimumSum2(grid, 0, i, 0, j)
                    + self.minimumSum2(grid, 0, i, j + 1, m - 1)
                    + self.minimumSum2(grid, i + 1, n - 1, 0, m - 1),
                )

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                result = min(
                    result,
                    self.minimumSum2(grid, 0, i, 0, m - 1)
                    + self.minimumSum2(grid, i + 1, j, 0, m - 1)
                    + self.minimumSum2(grid, j + 1, n - 1, 0, m - 1),
                )

        return result

    def minimumSum(self, grid: List[List[int]]) -> int:
        rgrid = self.rotate(grid)
        return min(self.solve(grid), self.solve(rgrid))


grid = [[1, 0, 1], [1, 1, 1]]
print(Solution().minimumSum(grid))
grid = [[1, 0, 1, 0], [0, 1, 0, 1]]
print(Solution().minimumSum(grid))
