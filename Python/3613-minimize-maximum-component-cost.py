# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, nodeX, nodeY):
        parentX, parentY = self.find(nodeX), self.find(nodeY)
        if parentX == parentY:
            return False
        self.parent[parentY] = parentX
        return True


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        tempEdges = []

        for u, v, w in edges:
            if uf.union(u, v):
                tempEdges.append(w)

        tempEdges.sort(reverse=True)
        for _ in range(k - 1):
            if tempEdges:
                tempEdges.pop(0)

        return tempEdges[0] if tempEdges else 0


n = 5
edges = [[0, 1, 4], [1, 2, 3], [1, 3, 2], [3, 4, 6]]
k = 2
print(Solution().minCost(n, edges, k))
n = 4
edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5]]
k = 1
print(Solution().minCost(n, edges, k))
