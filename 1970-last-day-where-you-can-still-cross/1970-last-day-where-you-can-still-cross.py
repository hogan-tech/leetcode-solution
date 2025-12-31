# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return

        if self.rank[rootX] > self.rank[rootY]:
            rootX, rootY = rootY, rootX
        self.parent[rootX] = rootY
        self.rank[rootY] += self.rank[rootX]


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = UnionFind(row * col + 2)
        grid = [[1] * col for _ in range(row)]

        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            grid[r][c] = 0
            index1 = r * col + c + 1
            for dR, dC in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR, newC = r + dR, c + dC
                index2 = newR * col + newC + 1
                if 0 <= newR < row and 0 <= newC < col and grid[newR][newC] == 0:
                    dsu.union(index1, index2)

            if r == 0:
                dsu.union(0, index1)
            if r == row - 1:
                dsu.union(row * col + 1, index1)
            if dsu.find(0) == dsu.find(row * col + 1):
                return i


row = 2
col = 2
cells = [[1, 1], [2, 1], [1, 2], [2, 2]]
print(Solution().latestDayToCross(row, col, cells))

row = 2
col = 2
cells = [[1, 1], [1, 2], [2, 1], [2, 2]]
print(Solution().latestDayToCross(row, col, cells))

row = 3
col = 3
cells = [[1, 2], [2, 1], [3, 3], [2, 2], [
    1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
print(Solution().latestDayToCross(row, col, cells))
