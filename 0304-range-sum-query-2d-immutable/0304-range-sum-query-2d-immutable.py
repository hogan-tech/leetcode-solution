# time complexity: O(1)
# space complexity: O(m*n)
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW = len(matrix)
        COL = len(matrix[0])
        if ROW == 0 or COL == 0:
            return
        self.preSum = [[0 for _ in range(COL + 1)] for _ in range(ROW + 1)]
        for r in range(ROW):
            for c in range(COL):
                self.preSum[r+1][c+1] = self.preSum[r][c+1] + \
                    self.preSum[r+1][c] + matrix[r][c] - self.preSum[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2+1][col2+1] + self.preSum[row1][col1] - self.preSum[row2 + 1][col1] - self.preSum[row1][col2 + 1]


numMatrix = NumMatrix([[3, 0, 1, 4, 2],
                       [5, 6, 3, 2, 1],
                       [1, 2, 0, 1, 5],
                       [4, 1, 0, 1, 7],
                       [1, 0, 3, 0, 5]])
print(numMatrix.sumRegion(2, 1, 4, 3))
print(numMatrix.sumRegion(1, 1, 2, 2))
print(numMatrix.sumRegion(1, 2, 2, 4))
