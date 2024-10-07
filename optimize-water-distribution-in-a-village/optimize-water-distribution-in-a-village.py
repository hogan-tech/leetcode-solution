# time complexity: O((n+m) * log(n + m))
# space compelxity: O(n + m)
from typing import List


class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size + 1)]
        self.rank = [1] * (size + 1)

    def find(self, node):
        if node == self.parents[node]:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            if self.rank[parentX] > self.rank[parentY]:
                self.parents[parentY] = parentX
            elif self.rank[parentY] > self.rank[parentX]:
                self.parents[parentX] = parentY
            else:
                self.parents[parentY] = parentX
                self.rank[parentX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        orderEdges = []
        for index, widget in enumerate(wells):
            orderEdges.append((widget, 0, index + 1))

        for startHouse, endHouse, weight in pipes:
            orderEdges.append((weight, startHouse, endHouse))

        orderEdges.sort(key=lambda x: x[0])

        disjointSet = UnionFind(n)
        total = 0
        for cost, house1, house2 in orderEdges:
            if not disjointSet.connected(house1, house2):
                disjointSet.union(house1, house2)
                total += cost
        return total


n = 3
wells = [1, 2, 2]
pipes = [[1, 2, 1], [2, 3, 1]]
print(Solution().minCostToSupplyWater(n, wells, pipes))
