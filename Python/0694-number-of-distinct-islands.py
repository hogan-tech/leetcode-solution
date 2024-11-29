# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            currentIsland.add((row - rowOrigin, col - colOrigin))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        seen = set()
        uniqueIslands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                currentIsland = set()
                rowOrigin = row
                colOrigin = col
                dfs(row, col)
                if currentIsland:
                    uniqueIslands.add(frozenset(currentIsland))

        return len(uniqueIslands)


grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
print(Solution().numDistinctIslands(grid))
