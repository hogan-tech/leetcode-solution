# time complexity: O(r*c)
# space complexity: O(r*c)
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        grid = [[None] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                grid[j][i] = matrix[i][j]
        return grid


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().transpose(matrix))
