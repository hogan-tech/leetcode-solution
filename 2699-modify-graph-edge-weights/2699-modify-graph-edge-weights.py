# time complexity: O(e*(v+e)logv)
# space complexity: O(e + v)
import heapq
import math
from typing import List, Tuple


class Solution:
    def modifiedGraphEdges(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
        target: int,
    ) -> List[List[int]]:
        INF = int(2e9)
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))

        currentShortestDistance = self.dijkstra(graph, source, destination)
        if currentShortestDistance < target:
            return []

        if currentShortestDistance == target:

            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF
            return edges

        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue
            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))
            newDistance = self.dijkstra(graph, source, destination)
            if newDistance <= target:
                edges[i][2] += target - newDistance
                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = INF
                return edges
        return []

    def dijkstra(
        self, graph: List[List[Tuple[int, int]]], src: int, destination: int
    ) -> int:
        minDistance = [math.inf] * len(graph)
        minDistance[src] = 0
        minHeap = [(0, src)]

        while minHeap:
            d, u = heapq.heappop(minHeap)
            if d > minDistance[u]:
                continue
            for v, w in graph[u]:
                if d + w < minDistance[v]:
                    minDistance[v] = d + w
                    heapq.heappush(minHeap, (minDistance[v], v))
        return minDistance[destination]


n = 3
edges = [[0, 1, -1], [0, 2, 5]]
source = 0
destination = 2
target = 6
print(Solution().modifiedGraphEdges(n, edges, source, destination, target))
