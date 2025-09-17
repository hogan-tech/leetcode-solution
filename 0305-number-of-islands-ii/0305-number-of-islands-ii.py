# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    class UnionFind:
        def __init__(self, size):
            self.parent = [i for i in range(size)]
            self.rank = [0 for _ in range(size)]
            self.count = 0

        def find(self, node):
            if node != self.parent[node]:
                self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

        def union(self, node1, node2):
            parent1 = self.find(node1)
            parent2 = self.find(node2)
            if parent1 != parent2:
                if self.rank[parent1] > self.rank[parent2]:
                    self.parent[parent2] = parent1
                elif self.rank[parent2] < self.rank[parent1]:
                    self.parent[parent1] = parent2
                else:
                    self.parent[parent2] = parent1
                    self.rank[parent1] += 1
                self.count -= 1

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        unionFind = self.UnionFind(m * n)
        result = []
        landMap = set()
        ROW = m
        COL = n
        for r, c in positions:
            if (r, c) in landMap:
                result.append(unionFind.count)
                continue

            landMap.add((r, c))
            unionFind.count += 1
            for dR, dC in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nextR, nextC = r + dR, c + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL and (nextR, nextC) in landMap:
                    unionFind.union(r * COL + c, nextR * COL + nextC)
            result.append(unionFind.count)
        return result


m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
print(Solution().numIslands2(m, n, positions))
m = 1
n = 1
positions = [[0, 0]]
print(Solution().numIslands2(m, n, positions))
