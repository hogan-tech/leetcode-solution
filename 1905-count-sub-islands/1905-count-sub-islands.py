# time complexity: O(m*n)
# space complexity: O(m*n)
from collections import deque
from typing import List


class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def isCellLand(self, x, y, grid):
        return grid[x][y] == 1

    def isSubIsland(self, x, y, grid1, grid2, visited):
        totalRows = len(grid2)
        totalCols = len(grid2[0])

        isSubIsland = True

        pendingCells = deque()
        pendingCells.append((x, y))
        visited[x][y] = True

        while pendingCells:
            currX, currY = pendingCells.popleft()

            if not self.isCellLand(currX, currY, grid1):
                isSubIsland = False

            for direction in self.directions:
                nextX = currX + direction[0]
                nextY = currY + direction[1]
                if (
                    0 <= nextX < totalRows
                    and 0 <= nextY < totalCols
                    and not visited[nextX][nextY]
                    and self.isCellLand(nextX, nextY, grid2)
                ):
                    pendingCells.append((nextX, nextY))
                    visited[nextX][nextY] = True
        return isSubIsland

    def countSubIslands(
        self, grid1: List[List[int]], grid2: List[List[int]]
    ) -> int:
        totalRows = len(grid2)
        totalCols = len(grid2[0])

        visited = [[False] * totalCols for _ in range(totalRows)]
        subIslandCounts = 0

        for x in range(totalRows):
            for y in range(totalCols):
                if (
                    not visited[x][y]
                    and self.isCellLand(x, y, grid2)
                    and self.isSubIsland(x, y, grid1, grid2, visited)
                ):
                    subIslandCounts += 1

        return subIslandCounts


grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [
    0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [
    0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]

print(Solution().countSubIslands(grid1, grid2))
