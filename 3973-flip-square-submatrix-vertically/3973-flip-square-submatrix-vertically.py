# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        result = [row[:] for row in grid]

        for r in range(k):
            originalRow = x + (k - 1 - r)
            finalRow = x + r
            for c in range(k):
                col = y + c
                result[finalRow][col] = grid[originalRow][col]

        return result


grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
x = 1
y = 0
k = 3
print(Solution().reverseSubmatrix(grid, x, y, k))
grid = [[3, 4, 2, 3], [2, 3, 4, 2]]
x = 0
y = 2
k = 2
print(Solution().reverseSubmatrix(grid, x, y, k))
