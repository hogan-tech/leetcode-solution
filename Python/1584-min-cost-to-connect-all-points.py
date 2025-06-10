# time complexity: O(n^2 logn)
# space complexity: O(n^2)
from heapq import heappop, heappush
from typing import List


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def join(self, node1: int, node2: int) -> bool:
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return False
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += 1
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
        result = 0
        edgesUsed = 0
        for weight, node1, node2 in allEdges:
            if uf.join(node1, node2):
                result += weight
                edgesUsed += 1
                if edgesUsed == n-1:
                    break
        return result


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        heap = [(0, 0)]

        inMst = [False] * n

        result = 0
        edgesUsed = 0

        while edgesUsed < n:
            weight, currNode = heappop(heap)

            if inMst[currNode]:
                continue

            inMst[currNode] = True
            result += weight
            edgesUsed += 1

            for nextNode in range(n):
                if not inMst[nextNode]:
                    nextWeight = abs(points[currNode][0] - points[nextNode][0]) +\
                        abs(points[currNode][1] - points[nextNode][1])

                    heappush(heap, (nextWeight, nextNode))

        return result


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
print(Solution().minCostConnectPoints(points))
