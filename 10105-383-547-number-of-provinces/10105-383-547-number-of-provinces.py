# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        result = 0
        seen = set()

        def dfs(city: int):
            for neighbor, connected in enumerate(isConnected[city]):
                if neighbor not in seen and connected == 1:
                    seen.add(neighbor)
                    dfs(neighbor)

        for city in range(len(isConnected)):
            if city not in seen:
                seen.add(city)
                dfs(city)
                result += 1
        return result

# time complexity: O(n^2)
# space complexity: O(n)
class UnionFind:
    def __init__(self, n):
        self.parents = [x for x in range(n)]
        self.count = [1 for _ in range(n)]
        self.groups = n

    def find(self, num):
        while num != self.parents[num]:
            self.parents[num] = self.parents[self.parents[num]]
            num = self.parents[num]
        return num

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX == rootY:
            return True

        if self.count[rootX] > self.count[rootY]:
            self.parents[rootY] = rootX
            self.count[rootX] += self.count[rootY]
        else:
            self.parents[rootX] = rootY
            self.count[rootY] += self.count[rootX]
        self.groups -= 1

        return False


class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n < 1 or len(grid[0]) != n:
            return 0
        union = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    union.union(i, j)
        return union.groups


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(Solution().findCircleNum(isConnected))
