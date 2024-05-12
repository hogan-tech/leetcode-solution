# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import List


class Solution:
    def findMaxValue(self, grid: List[List[int]], i: int, j: int) -> int:
        maxVal = 0
        for a in range(i, i + 3):
            for b in range(j, j + 3):
                maxVal = max(grid[a][b], maxVal)
        return maxVal

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = [[0] * (len(grid) - 2) for _ in range(len(grid[0]) - 2)]
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                result[i][j] = self.findMaxValue(grid, i, j)
        return result


grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
print(Solution().largestLocal(grid))
