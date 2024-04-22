# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    class UnionFind:
        def __init__(self, size):
            self.rep = [i for i in range(size)]
            self.rank = [0] * size
            self.count = 0

        def find(self, node):
            if node != self.rep[node]:
                self.rep[node] = self.find(self.rep[node])
            return self.rep[node]

        def union(self, node1, node2):
            rep1 = self.find(node1)
            rep2 = self.find(node2)
            if rep1 != rep2:
                if self.rank[rep1] > self.rank[rep2]:
                    self.rep[rep2] = rep1
                elif self.rank[rep2] < self.rank[rep1]:
                    self.rep[rep1] = rep2
                else:
                    self.rep[rep2] = rep1
                    self.rank[rep1] += 1
                self.count -= 1

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = self.UnionFind(m * n)
        res = []
        land_map = set()

        for row, col in positions:
            if (row, col) in land_map:
                res.append(uf.count)
                continue

            land_map.add((row, col))
            uf.count += 1

            for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                r, c = row + i, col + j
                if r < 0 or c < 0 or r >= m or c >= n:
                    continue
                if (r, c) in land_map:
                    uf.union(row * n + col, r * n + c)

            res.append(uf.count)

        return res


m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
print(Solution().numIslands2(m, n, positions))
