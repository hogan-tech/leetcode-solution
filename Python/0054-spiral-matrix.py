# time complexity: O(m*n)
# space complexity: O(1)
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROW = len(matrix)
        COL = len(matrix[0])
        direction = 1
        row = 0
        col = -1
        result = []
        while ROW > 0 and COL > 0:
            for _ in range(COL):
                col += direction
                result.append(matrix[row][col])
            ROW -= 1
            for _ in range(ROW):
                row += direction
                result.append(matrix[row][col])
            COL -= 1

            direction *= -1

        return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().spiralOrder(matrix))
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(Solution().spiralOrder(matrix))
