# time complexity: O(n + mlogm)
# space complexity: O(n + m)
from typing import List
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, 2 * w))

        dist = [float('inf')] * n
        visited = [False] * n
        dist[0] = 0
        heap = [(0, 0)]

        while heap:
            cur_dist, x = heapq.heappop(heap)

            if x == n - 1:
                return cur_dist

            if visited[x]:
                continue
            visited[x] = True

            for y, w in g[x]:
                new_dist = cur_dist + w
                if new_dist < dist[y]:
                    dist[y] = new_dist
                    heapq.heappush(heap, (new_dist, y))

        return -1


n = 4
edges = [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]
print(Solution().minCost(n, edges))
n = 4
edges = [[0, 2, 1], [2, 1, 1], [1, 3, 1], [2, 3, 3]]
print(Solution().minCost(n, edges))
