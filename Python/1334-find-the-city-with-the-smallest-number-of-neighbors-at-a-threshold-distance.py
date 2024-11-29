# time complexity: O(n^3*logn)
# space complexity: O(n^2)
import heapq
from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:

        adjacencyList = [[] for _ in range(n)]

        shortestPathMatrix = [[float("inf")] * n for _ in range(n)]

        for i in range(n):
            shortestPathMatrix[i][i] = 0

        for start, end, weight in edges:
            adjacencyList[start].append((end, weight))
            adjacencyList[end].append((start, weight))

        for i in range(n):
            self.dijkstra(n, adjacencyList, shortestPathMatrix[i], i)

        return self.getCityWithFewestReachable(
            n, shortestPathMatrix, distanceThreshold
        )

    def dijkstra(
        self,
        n: int,
        adjacencyList: List[List[tuple]],
        shortestPathDistances: List[int],
        source: int,
    ):

        priorityQueue = [(0, source)]
        shortestPathDistances[:] = [float("inf")] * n
        shortestPathDistances[source] = 0

        while priorityQueue:
            currentDistance, currentCity = heapq.heappop(priorityQueue)
            if currentDistance > shortestPathDistances[currentCity]:
                continue

            for neighborCity, edgeWeight in adjacencyList[currentCity]:
                if (
                    shortestPathDistances[neighborCity]
                    > currentDistance + edgeWeight
                ):
                    shortestPathDistances[neighborCity] = (
                        currentDistance + edgeWeight
                    )
                    heapq.heappush(
                        priorityQueue,
                        (shortestPathDistances[neighborCity],
                         neighborCity),
                    )

    def getCityWithFewestReachable(
        self,
        n: int,
        shortestPathMatrix: List[List[int]],
        distanceThreshold: int,
    ) -> int:
        cityWithFewestReachable = -1
        fewestReachableCount = n

        for i in range(n):
            reachableCount = sum(
                1
                for j in range(n)
                if i != j and shortestPathMatrix[i][j] <= distanceThreshold
            )

            if reachableCount <= fewestReachableCount:
                fewestReachableCount = reachableCount
                cityWithFewestReachable = i
        return cityWithFewestReachable


n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
print(Solution().findTheCity(n, edges, distanceThreshold))
