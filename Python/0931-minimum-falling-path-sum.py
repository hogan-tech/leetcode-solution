# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}

        def findMinFallingPathSum(row: int, col: int) -> int:
            if col < 0 or col >= len(matrix):
                return float('inf')
            if row == len(matrix) - 1:
                return matrix[row][col]
            if (row, col) in memo:
                return memo[(row, col)]

            left = findMinFallingPathSum(row+1, col-1)
            middle = findMinFallingPathSum(row+1, col)
            right = findMinFallingPathSum(row+1, col+1)

            memo[(row, col)] = min(left, middle, right) + matrix[row][col]
            return memo[(row, col)]

        minFallingSum = float('inf')
        for startCol in range(len(matrix)):
            minFallingSum = min(
                minFallingSum, findMinFallingPathSum(0, startCol))
        return minFallingSum


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(Solution().minFallingPathSum(matrix))
