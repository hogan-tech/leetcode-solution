# time complexity: O((E+V) * a(V) + VlogV)
# space complexity: O(V)
# each union-find operation: O(a(V)) The Inverse Ackermann Function 
from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX != parentY:
            if self.rank[parentX] > self.rank[parentY]:
                self.parent[parentY] = parentX
            elif self.rank[parentX] < self.rank[parentY]:
                self.parent[parentX] = parentY
            else:
                self.parent[parentY] = parentX
                self.rank[parentX] += 1

    def connected(self, x, y):
        return self.find[x] == self.find[y]


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        disjointSet = UnionFind(len(s))
        for startVertex, endVertex in pairs:
            disjointSet.union(startVertex, endVertex)

        rootToComponent = defaultdict(list)
        for i in range(len(s)):
            root = disjointSet.find(i)
            rootToComponent[root].append(i)

        for _, indices in rootToComponent.items():
            chars = []
            for i in indices:
                chars.append(s[i])
            chars = sorted(chars)

            for c, i in zip(chars, indices):
                s[i] = c

        return "".join(s)


s = "dcab"
pairs = [[0, 3], [1, 2]]
print(Solution().smallestStringWithSwaps(s, pairs))
