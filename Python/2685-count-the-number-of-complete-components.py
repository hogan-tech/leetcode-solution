# time complexity: O(n + m*a(n))
# space complexity: O(n)
from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, size):
        self.parents = [-1] * size
        self.size = [1] * size

    def find(self, node):
        if self.parents[node] == -1:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            return

        if self.size[parentX] > self.size[parentY]:
            self.parents[parentY] = parentX
            self.size[parentX] += self.size[parentY]
        else:
            self.parents[parentX] = parentY
            self.size[parentY] += self.size[parentX]


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        edgeCount = defaultdict(int)
        for x, y in edges:
            uf.union(x, y)

        for x, _ in edges:
            root = uf.find(x)
            edgeCount[root] += 1

        completeCount = 0
        for vertex in range(n):
            if uf.find(vertex) == vertex:
                nodeCount = uf.size[vertex]
                expectedEdges = (nodeCount * (nodeCount - 1)) // 2
                if edgeCount[vertex] == expectedEdges:
                    completeCount += 1

        return completeCount


n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
print(Solution().countCompleteComponents(n, edges))
n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
print(Solution().countCompleteComponents(n, edges))
