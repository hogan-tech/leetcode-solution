# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        minRC = [float('inf'), float('inf')]
        maxRC = [-float('inf'), -float('inf')]
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    minRC = [min(minRC[0], r), min(minRC[1], c)]
                    maxRC = [max(maxRC[0], r), max(maxRC[1], c)]

        return (maxRC[0] - minRC[0] + 1) * (maxRC[1] - minRC[1] + 1)


grid = [[0, 1, 0], [1, 0, 1]]
print(Solution().minimumArea(grid))
grid = [[1, 0], [0, 0]]
print(Solution().minimumArea(grid))
