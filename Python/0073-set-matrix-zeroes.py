# time complexity: O(m*n)
# space complexity: O(m+n)
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowSet, colSet = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowSet or j in colSet:
                    matrix[i][j] = 0
        return matrix


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(Solution().setZeroes(matrix))
