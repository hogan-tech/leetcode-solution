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
            


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(Solution().setZeroes(matrix))
