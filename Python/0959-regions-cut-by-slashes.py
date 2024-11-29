# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        gridSize = len(grid)
        pointsPerSide = gridSize + 1
        totalPoints = pointsPerSide * pointsPerSide
        parentArray = [-1] * totalPoints
        for i in range(pointsPerSide):
            for j in range(pointsPerSide):
                if (
                    i == 0
                    or j == 0
                    or i == pointsPerSide - 1
                    or j == pointsPerSide - 1
                ):
                    point = i * pointsPerSide + j
                    parentArray[point] = 0
        parentArray[0] = -1
        regionCount = 1
        for i in range(gridSize):
            for j in range(gridSize):
                if grid[i][j] == "/":
                    topRight = i * pointsPerSide + (j + 1)
                    bottomLeft = (i + 1) * pointsPerSide + j
                    regionCount += self.union(
                        parentArray, topRight, bottomLeft
                    )
                elif grid[i][j] == "\\":
                    topLeft = i * pointsPerSide + j
                    bottomRight = (i + 1) * pointsPerSide + (j + 1)
                    regionCount += self.union(
                        parentArray, topLeft, bottomRight
                    )
        return regionCount

    def find(self, parentArray: List[int], node: int) -> int:
        if parentArray[node] == -1:
            return node
        parentArray[node] = self.find(parentArray, parentArray[node])
        return parentArray[node]

    def union(self, parentArray: List[int], node1: int, node2: int) -> int:
        parent1 = self.find(parentArray, node1)
        parent2 = self.find(parentArray, node2)
        if parent1 == parent2:
            return 1
        parentArray[parent2] = parent1
        return 0


grid = [" /", "/ "]
print(Solution().regionsBySlashes(grid))
