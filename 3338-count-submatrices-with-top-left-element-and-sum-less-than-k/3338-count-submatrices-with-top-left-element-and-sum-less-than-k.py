# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        prefix = [[0 for _ in range(COL)] for _ in range(ROW)]
        prefix[0][0] = grid[0][0]
        for r in range(1, ROW):
            prefix[r][0] = grid[r][0] + prefix[r-1][0]

        for c in range(1, COL):
            prefix[0][c] = grid[0][c] + prefix[0][c-1]

        for r in range(1, ROW):
            for c in range(1, COL):
                prefix[r][c] = grid[r][c] + prefix[r-1][c] + \
                    prefix[r][c-1] - prefix[r-1][c-1]

        count = 0
        for r in range(ROW):
            for c in range(COL):
                if prefix[r][c] <= k:
                    count += 1
        return count


'''
 7 13 19
13 25 29
'''
grid = [[7, 6, 3], [6, 6, 1]]
k = 18
print(Solution().countSubmatrices(grid, k))
grid = [[7, 2, 9], [1, 5, 0], [2, 6, 6]]
k = 20
print(Solution().countSubmatrices(grid, k))
