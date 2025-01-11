# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        nR = len(grid)
        nC = len(grid[0])
        grid[r][c] = '0'
        if r - 1 >= 0 and grid[r - 1][c] == "1":
            self.dfs(grid, r - 1, c)
        if r + 1 < nR and grid[r + 1][c] == "1":
            self.dfs(grid, r + 1, c)
        if c - 1 >= 0 and grid[r][c - 1] == "1":
            self.dfs(grid, r, c - 1)
        if c + 1 < nC and grid[r][c + 1] == "1":
            self.dfs(grid, r, c + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        numIslands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    numIslands += 1
                    self.dfs(grid, r, c)
        return numIslands


class UnionFind:
    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0
        ROW = len(grid)
        COL = len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    self.parent.append(r * COL + c)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return True
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        self.count -= 1

    def getCount(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        unionFind = UnionFind(grid)
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    if r + 1 < ROW and grid[r + 1][c] == '1':
                        unionFind.union(r * COL + c, (r + 1) * COL + c)
                    if c + 1 < COL and grid[r][c + 1] == '1':
                        unionFind.union(r * COL + c, r * COL + c + 1)
        count = unionFind.getCount()
        return count


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(Solution().numIslands(grid))
