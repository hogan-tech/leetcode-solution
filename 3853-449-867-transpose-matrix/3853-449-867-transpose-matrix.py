# time complexity: O(r*c)
# space complexity: O(r*c)
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROW = len(matrix)
        COL = len(matrix[0])
        grid = [[0 for _ in range(ROW)] for _ in range(COL)]
        for r in range(ROW):
            for c in range(COL):
                grid[c][r] = matrix[r][c]
        return grid


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().transpose(matrix))
matrix = [[1, 2, 3], [4, 5, 6]]
print(Solution().transpose(matrix))
