# time complexity: O(u*v)
# space complexity: O(u*v)
from heapq import heappop, heappush
from typing import List
from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, start, end in edges:
            graph[u].append((v, start, end))

        heap = [(0, 0)]
        visitedTime = [float('inf')] * n
        visitedTime[0] = 0

        while heap:
            currTime, u = heappop(heap)

            if u == n - 1:
                return currTime

            if currTime > visitedTime[u]:
                continue

            for v, start, end in graph[u]:
                if currTime <= end:
                    waitTime = max(currTime, start)
                    arriveTime = waitTime + 1

                    if arriveTime < visitedTime[v]:
                        visitedTime[v] = arriveTime
                        heappush(heap, (arriveTime, v))

        return -1


n = 3
edges = [[0, 1, 0, 1], [1, 2, 2, 5]]
print(Solution().minTime(n, edges))
n = 4
edges = [[0, 1, 0, 3], [1, 3, 7, 8], [0, 2, 1, 5], [2, 3, 4, 7]]
print(Solution().minTime(n, edges))
n = 3
edges = [[1, 0, 1, 3], [1, 2, 3, 5]]
print(Solution().minTime(n, edges))
