# time complexity: O(m*n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def getHourglassSum(row, col):
            top = grid[row - 1][col - 1] + \
                grid[row - 1][col] + grid[row - 1][col + 1]
            bottom = grid[row + 1][col - 1] + \
                grid[row + 1][col] + grid[row + 1][col + 1]
            middle = grid[row][col]

            return top + bottom + middle
        ROW = len(grid)
        COL = len(grid[0])
        maxSum = 0
        for r in range(1, ROW - 1):
            for c in range(1, COL - 1):
                maxSum = max(maxSum, getHourglassSum(r, c))
        return maxSum


grid = [[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]
print(Solution().maxSum(grid))
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().maxSum(grid))
