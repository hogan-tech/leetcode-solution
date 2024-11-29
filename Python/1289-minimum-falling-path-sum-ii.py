# time complexity: O(n^3)
# space complexity: O(n^2)
from cmath import inf
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = {}

        def optimal(row, col):
            if row == n - 1:
                return grid[row][col]

            if (row, col) in memo:
                return memo[(row, col)]

            next_minimum = inf
            for next_row_col in range(n):
                if next_row_col != col:
                    next_minimum = min(
                        next_minimum, optimal(row + 1, next_row_col))
            memo[(row, col)] = grid[row][col] + next_minimum
            return memo[(row, col)]

        answer = inf
        for col in range(n):
            answer = min(answer, optimal(0, col))
        return answer


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().minFallingPathSum(grid))
