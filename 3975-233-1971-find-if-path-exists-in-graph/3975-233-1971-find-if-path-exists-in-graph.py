# time complexity: O(n+m)
# space complexity: O(n+m)
from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n

        def dfs(currNode):
            if currNode == destination:
                return True
            if not seen[currNode]:
                seen[currNode] = True
                for nextNode in graph[currNode]:
                    if dfs(nextNode):
                        return True
            return False
        return dfs(source)

# time complexity: O(m*a(n))
# space complexity: O(n)
class UnionFind:
    def __init__(self, n):
        self.parent = [num for num in range(n + 1)]
        self.rank = [1] * n

    def find(self, num):
        if num != self.parent[num]:
            self.parent[num] = self.find(self.parent[num])
        return self.parent[num]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        return uf.find(source) == uf.find(destination)


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
print(Solution().validPath(n, edges, source, destination))
n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5
print(Solution().validPath(n, edges, source, destination))
