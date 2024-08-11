# time complexity: O((mn)^2)
# space complexity: O(m*n)
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def countIslands():
            visited = set()
            count = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        exploreIsland(i, j, visited)
                        count += 1
            return count

        def exploreIsland(i, j, visited):
            if (
                i < 0
                or i >= rows
                or j < 0
                or j >= cols
                or grid[i][j] == 0
                or (i, j) in visited
            ):
                return
            visited.add((i, j))
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                exploreIsland(i + di, j + dj, visited)

        if countIslands() != 1:
            return 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if countIslands() != 1:
                        return 1
                    grid[i][j] = 1

        return 2


grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(Solution().minDays(grid))
