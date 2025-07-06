# time complexity: O(E * log W)
# space complexity: O(N)
from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0 for _ in range(size)]
        self.count = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xParent = self.find(x)
        yParent = self.find(y)
        if xParent == yParent:
            return
        if self.rank[xParent] < self.rank[yParent]:
            self.parent[xParent] = yParent
        else:
            self.parent[yParent] = xParent
            if self.rank[xParent] == self.rank[yParent]:
                self.rank[xParent] += 1
        self.count -= 1


class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        if k == 1:
            return 0
        if n < k:
            return -1

        uf = UnionFind(n)
        for u, v, time in edges:
            uf.union(u, v)
        if uf.count >= k:
            return 0

        left = 0
        right = max(edge[2] for edge in edges) if edges else 0

        answer = right

        edgesSorted = sorted(edges, key=lambda x: x[2])

        left = 0
        right = edgesSorted[-1][2] if edges else 0

        answer = right

        while left <= right:
            mid = (left + right) // 2
            uf = UnionFind(n)
            for u, v, time in edges:
                if time > mid:
                    uf.union(u, v)
            if uf.count >= k:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer


n = 2
edges = [[0, 1, 3]]
k = 2
print(Solution().minTime(n, edges, k))
n = 3
edges = [[0, 1, 2], [1, 2, 4]]
k = 3
print(Solution().minTime(n, edges, k))
n = 3
edges = [[0, 2, 5]]
k = 2
print(Solution().minTime(n, edges, k))
