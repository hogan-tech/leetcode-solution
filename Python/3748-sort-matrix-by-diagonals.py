# time complextity: O(n^2)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonal = defaultdict(list)
        for r in range(n):
            for c in range(n):
                diagonal[r - c].append(grid[r][c])

        for key in diagonal:
            if key < 0:
                diagonal[key].sort()
            else:
                diagonal[key].sort(reverse=True)

        for r in range(n):
            for c in range(n):
                grid[r][c] = diagonal[r-c].pop(0)

        return grid


grid = [[1, 7, 3], [9, 8, 2], [4, 5, 6]]
print(Solution().sortMatrix(grid))
grid = [[0, 1], [1, 2]]
print(Solution().sortMatrix(grid))
grid = [[1]]
print(Solution().sortMatrix(grid))
