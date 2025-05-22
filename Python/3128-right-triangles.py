# time complexity: O(n*m + k)
# space complexity: O(k)
from typing import List
from collections import defaultdict


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        blocks = []
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]:
                    blocks.append((r, c))

        xCount = defaultdict(int)
        yCount = defaultdict(int)
        for r, c in blocks:
            xCount[r] += 1
            yCount[c] += 1

        count = 0
        for r, c in blocks:
            count += (xCount[r] - 1) * (yCount[c] - 1)

        return count


grid = [[0, 1, 0], [0, 1, 1], [0, 1, 0]]
print(Solution().numberOfRightTriangles(grid))
grid = [[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
print(Solution().numberOfRightTriangles(grid))
grid = [[1, 0, 1], [1, 0, 0], [1, 0, 0]]
print(Solution().numberOfRightTriangles(grid))
grid = [[0, 0], [0, 1], [1, 1]]
print(Solution().numberOfRightTriangles(grid))
