# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class DisjointSet:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.islandSize = [1] * n

    def findRoot(self, node: int) -> int:

        if self.parent[node] == node:
            return node

        self.parent[node] = self.findRoot(self.parent[node])
        return self.parent[node]

    def unionNodes(self, nodeA: int, nodeB: int):

        rootA = self.findRoot(nodeA)
        rootB = self.findRoot(nodeB)

        if rootA == rootB:
            return

        if self.islandSize[rootA] < self.islandSize[rootB]:
            self.parent[rootA] = rootB
            self.islandSize[rootB] += self.islandSize[rootA]
        else:
            self.parent[rootB] = rootA
            self.islandSize[rootA] += self.islandSize[rootB]


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        ds = DisjointSet(ROW * COL)

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    currentNode = (COL * row) + col
                    for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        nextR = row + dR
                        nextC = col + dC

                        if (0 <= nextR < ROW and 0 <= nextC < COL and grid[nextR][nextC] == 1):
                            neighborNode = COL * nextR + nextC
                            ds.unionNodes(currentNode, neighborNode)

        maxSize = 0

        hasZero = False

        uniqueRoots = set()

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 0:
                    hasZero = True

                    currentIslandSize = 1

                    for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        nextR = row + dR
                        nextC = col + dC

                        if (
                            0 <= nextR < ROW
                            and 0 <= nextC < COL
                            and grid[nextR][nextC] == 1
                        ):
                            neighborNode = (
                                COL * nextR + nextC
                            )

                            root = ds.findRoot(neighborNode)
                            uniqueRoots.add(root)

                    for root in uniqueRoots:
                        currentIslandSize += ds.islandSize[root]

                    uniqueRoots.clear()

                    maxSize = max(maxSize, currentIslandSize)

        if not hasZero:
            return ROW * COL
        return maxSize


grid = [[1, 0], [0, 1]]
print(Solution().largestIsland(grid))
grid = [[1, 1], [1, 0]]
print(Solution().largestIsland(grid))
grid = [[1, 1], [1, 1]]
print(Solution().largestIsland(grid))
