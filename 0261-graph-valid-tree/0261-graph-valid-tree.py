# time complexity: O(n)
# space complexity: O(n)
from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = list(range(n))

    def find(self, node: int) -> int:
        while node != self.parents[node]:
            node = self.parents[node]
        return node

    def union(self, nodeX: int, nodeY: int) -> bool:
        parentX, parentY = self.find(nodeX), self.find(nodeY)
        if parentX == parentY:
            return False
        self.parents[parentX] = parentY
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        disjointUnionSet = UnionFind(n)
        for startVertex, endVertex in edges:
            if not disjointUnionSet.union(startVertex, endVertex):
                return False
        return True


n = 5
edges = [[0, 1], [0, 2], [0, 3], [2, 3]]
print(Solution().validTree(n, edges))
