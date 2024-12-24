# time complexity: O(n+m)
# space complexity: O(n+m)
from collections import deque
from math import ceil
from typing import List


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        n = len(edges1) + 1
        m = len(edges2) + 1

        adjList1 = self.buildAdjList(n, edges1)
        adjList2 = self.buildAdjList(m, edges2)

        diameter1 = self.findDiameter(n, adjList1)
        diameter2 = self.findDiameter(m, adjList2)

        combinedDiameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        return max(diameter1, diameter2, combinedDiameter)

    def buildAdjList(self, size, edges):
        adjList = [[] for _ in range(size)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        return adjList

    def findDiameter(self, n, adjList):
        farthestNode, _ = self.findFarthestNode(n, adjList, 0)

        _, diameter = self.findFarthestNode(n, adjList, farthestNode)
        return diameter

    def findFarthestNode(self, n, adjList, sourceNode):
        queue = deque([sourceNode])
        visited = [False] * n
        visited[sourceNode] = True

        maximumDistance = 0
        farthestNode = sourceNode

        while queue:
            for _ in range(len(queue)):
                currentNode = queue.popleft()
                farthestNode = currentNode

                for neighbor in adjList[currentNode]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

            if queue:
                maximumDistance += 1

        return farthestNode, maximumDistance


edges1 = [[0, 1], [0, 2], [0, 3]]
edges2 = [[0, 1]]
print(Solution().minimumDiameterAfterMerge(edges1, edges2))
