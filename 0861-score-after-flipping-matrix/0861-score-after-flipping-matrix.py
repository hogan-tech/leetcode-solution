# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            if grid[i][0] == 0:
                for j in range(col):
                    grid[i][j] ^= 1

        for j in range(1, col):
            countZero = 0
            for i in range(row):
                if grid[i][j] == 0:
                    countZero += 1

            if countZero > row - countZero:
                for i in range(row):
                    grid[i][j] ^= 1

        score = 0
        for i in range(row):
            for j in range(col):
                colScore = grid[i][j] << (col-j-1)
                score += colScore

        return score


grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
print(Solution().matrixScore(grid))
