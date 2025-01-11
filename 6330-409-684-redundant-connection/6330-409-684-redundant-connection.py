# time complexity: O(n)
# space complexity: O(n)
from typing import List


class UnionFind:
    def __init__(self, countNodes: int) -> None:
        self.parents = list(range(countNodes + 1))
        self.ranks = [1] * (countNodes + 1)

    def find(self, node: int) -> int:
        while node != self.parents[node]:
            node = self.parents[node]
            self.parents[node] = self.parents[self.parents[node]]
        return self.parents[node]

    def union(self, nodeX: int, nodeY: int) -> bool:
        parentX, parentY = self.find(nodeX), self.find(nodeY)
        if parentX == parentY:
            return False
        elif self.ranks[parentX] > self.ranks[parentY]:
            self.ranks[parentX] += self.ranks[parentY]
            self.parents[parentY] = parentX
        else:
            self.ranks[parentY] += self.ranks[parentX]
            self.parents[parentX] = parentY
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjointSet = UnionFind(len(edges))
        for start, end in edges:
            if not disjointSet.union(start, end):
                return [start, end]


edges = [[1, 2], [1, 3], [2, 3]]
print(Solution().findRedundantConnection(edges))
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print(Solution().findRedundantConnection(edges))
