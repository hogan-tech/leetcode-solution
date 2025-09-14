# time complexity: O(m*n)
# space complexity: O(m+n)
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowSet, colSet = set(), set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rowSet.add(r)
                    colSet.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rowSet or c in colSet:
                    matrix[r][c] = 0

# time complexity: O(r*c)
# space complexity: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW = len(matrix)
        COL = len(matrix[0])
        firstRowZero = False        
        firstColZero = False
        for c in range(COL):
            if matrix[0][c] == 0:
                firstRowZero = True
                break
        for r in range(ROW):
            if matrix[r][0] == 0:
                firstColZero = True
                break
        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, ROW):
            if matrix[r][0] == 0:
                for c in range(1, COL):
                    matrix[r][c] = 0
        for c in range(1, COL):
            if matrix[0][c] == 0:
                for r in range(1, ROW):
                    matrix[r][c] = 0
        if firstRowZero:
            for c in range(COL):
                matrix[0][c] = 0
        if firstColZero:
            for r in range(ROW):
                matrix[r][0] = 0
        return matrix


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(Solution().setZeroes(matrix))
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(Solution().setZeroes(matrix))
