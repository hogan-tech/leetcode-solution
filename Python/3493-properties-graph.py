# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = [n for n in range(size)]
        self.rank = [1] * size
        return

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
        return

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        m = len(properties[0])

        def intersect(aArr, bArr):
            return len(set(aArr).intersection(set(bArr)))

        uf = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if intersect(properties[i], properties[j]) >= k:
                    uf.union(i, j)

        return len(set(uf.parent))


properties = [[1, 2], [1, 1], [3, 4], [4, 5], [5, 6], [7, 7]]
k = 1
print(Solution().numberOfComponents(properties, k))
properties = [[1, 2, 3], [2, 3, 4], [4, 3, 5]]
k = 2
print(Solution().numberOfComponents(properties, k))
properties = [[1, 1], [1, 1]]
k = 2
print(Solution().numberOfComponents(properties, k))
