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
        return self.parents[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if self.rank[parent1] > self.rank[parent2]:
            self.parents[parent2] = parent1
        elif self.rank[parent1] < self.rank[parent2]:
            self.parents[parent1] = parent2
        else:
            self.parents[parent1] = parent2
            self.rank[parent2] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)

        parent = set()
        for node in range(n):
            parent.add(uf.find(node))
        return len(set(parent))


n = 4
edges = [[0, 1], [2, 3], [1, 2]]
print(Solution().countComponents(n, edges))
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(Solution().countComponents(n, edges))
n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
print(Solution().countComponents(n, edges))
