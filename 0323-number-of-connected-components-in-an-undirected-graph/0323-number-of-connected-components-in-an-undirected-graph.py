# time complexity: O(V + E * α(n)) is the inverse Ackermann function
# space complexity: O(V)
from typing import List


class UnionFind():
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, node):
        while node != self.parents[node]:
            node = self.parents[node]
        return node

    def uion(self, nodeX, nodeY):
        parentX = self.find(nodeX)
        parentY = self.find(nodeY)

        if parentX == parentY:
            return

        if self.rank[parentX] > self.rank[parentY]:
            self.parents[parentY] = self.parents[parentX]
        elif self.rank[parentX] < self.rank[parentY]:
            self.parents[parentX] = self.parents[parentY]
        else:
            self.parents[parentX] = self.parents[parentY]
            self.rank[parentY] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjointUnionSet = UnionFind(n)
        for startVertex, endVertex in edges:
            disjointUnionSet.uion(startVertex, endVertex)

        parent = set()
        for i in range(n):
            parent.add(disjointUnionSet.find(i))
        return len(set(parent))


n = 4
edges = [[0, 1], [2, 3], [1, 2]]
print(Solution().countComponents(n, edges))
