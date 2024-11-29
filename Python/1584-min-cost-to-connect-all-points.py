from typing import List


class UnionFind:
    def __init__(self, size: int) -> None:
        self.group = [0]*size
        self.rank = [0]*size
        for i in range(size):
            self.group[i] = i

    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)

        if group1 == group2:
            return False
        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1
        return True


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        allEdges = []

        for currNode in range(n):
            for nextNode in range(currNode + 1, n):
                weight = abs(points[currNode][0] - points[nextNode][0]) + \
                    abs(points[currNode][1] - points[nextNode][1])
                allEdges.append((weight, currNode, nextNode))

        allEdges.sort()

        uf = UnionFind(n)
        mstCost = 0
        edgesUsed = 0
        for weight, node1, node2 in allEdges:
            if uf.join(node1, node2):
                mstCost += weight
                edgesUsed += 1
                if edgesUsed == n-1:
                    break
        return mstCost


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
print(Solution().minCostConnectPoints(points))
