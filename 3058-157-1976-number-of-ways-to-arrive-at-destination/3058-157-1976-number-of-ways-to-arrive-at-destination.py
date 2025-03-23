# time complexity: O((n + e)logn)
# space complexity: O(n + e)
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        adjList = defaultdict(list)
        for inNode, outNode, weight in roads:
            adjList[inNode].append((outNode, weight))
            adjList[outNode].append((inNode, weight))

        pq = []
        heappush(pq, (0, 0))

        pathCount = [0] * n
        pathCount[0] = 1

        shortestTime = [float('inf')] * n
        shortestTime[0] = 0

        while pq:
            currWeight, currNode = heappop(pq)
            if currWeight > shortestTime[currNode]:
                continue

            for nextNode, weight in adjList[currNode]:
                nextWeight = currWeight + weight
                if nextWeight < shortestTime[nextNode]:
                    shortestTime[nextNode] = nextWeight
                    pathCount[nextNode] = pathCount[currNode]
                    heappush(pq, [nextWeight, nextNode])
                elif nextWeight == shortestTime[nextNode]:
                    pathCount[nextNode] = (
                        pathCount[nextNode] + pathCount[currNode]) % MOD

        return pathCount[n - 1]


n = 7
roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3],
         [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
print(Solution().countPaths(n, roads))
n = 2
roads = [[1, 0, 10]]
print(Solution().countPaths(n, roads))
