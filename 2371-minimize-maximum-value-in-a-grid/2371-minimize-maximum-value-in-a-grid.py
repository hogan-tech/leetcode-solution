# time complexity: O(m*nlogn)
# space complexity: O(mn)
from typing import List


class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        ROW = len(grid)
        COL = len(grid[0])

        rows = [1] * ROW
        cols = [1] * COL

        temp = []
        for i in range(ROW):
            for j in range(COL):
                temp.append((grid[i][j], i, j))
        temp.sort()
        for item in temp:
            _, i, j = item
            value = max(rows[i], cols[j])
            grid[i][j] = value
            rows[i] = value + 1
            cols[j] = value + 1
        return grid


grid = [[3, 1], [2, 5]]
print(Solution().minScore(grid))
grid = [[10]]
print(Solution().minScore(grid))
grid = [[2, 4, 5], [7, 3, 9]]
print(Solution().minScore(grid))
