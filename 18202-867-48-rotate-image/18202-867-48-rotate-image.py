from typing import List

# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROW = len(matrix)
        COL = len(matrix[0])
        newMatrix = [[0 for _ in range(COL)]
                     for _ in range(ROW)]

        for r in range(ROW):
            for c in range(COL):
                newMatrix[c][ROW - r - 1] = matrix[r][c]
        return

# time complexity: O(n^2)
# space complexity: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n // 2):
            for c in range(r, n - r - 1):
                matrix[r][c], matrix[c][n-1-r] = matrix[c][n-1-r], matrix[r][c]
                matrix[r][c], matrix[n-1-r][n-1 -
                                            c] = matrix[n-1-r][n-1-c], matrix[r][c]
                matrix[r][c], matrix[n-1-c][r] = matrix[n-1-c][r], matrix[r][c]
        return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().rotate(matrix))
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(Solution().rotate(matrix))
