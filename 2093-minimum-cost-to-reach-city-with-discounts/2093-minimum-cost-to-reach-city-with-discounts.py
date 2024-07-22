# time complexity: O((n*k + e)log(n*k))
# space complexity: O(n*k + e)
import heapq
from typing import List


class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = [[] for _ in range(n)]
        for highway in highways:
            u, v, toll = highway
            graph[u].append((v, toll))
            graph[v].append((u, toll))
        pq = [(0, 0, 0)]
        dist = [[float("inf")] * (discounts + 1) for _ in range(n)]
        dist[0][0] = 0
        visited = [[False] * (discounts + 1) for _ in range(n)]
        while pq:
            currentCost, city, discountsUsed = heapq.heappop(pq)
            if visited[city][discountsUsed]:
                continue
            visited[city][discountsUsed] = True
            for neighbor, toll in graph[city]:
                if currentCost + toll < dist[neighbor][discountsUsed]:
                    dist[neighbor][discountsUsed] = currentCost + toll
                    heapq.heappush(
                        pq, (dist[neighbor][discountsUsed], neighbor, discountsUsed))

                if discountsUsed < discounts:
                    newCostWithDiscount = currentCost + toll // 2
                    if (newCostWithDiscount < dist[neighbor][discountsUsed + 1]):
                        dist[neighbor][
                            discountsUsed + 1
                        ] = newCostWithDiscount
                        heapq.heappush(
                            pq, (newCostWithDiscount, neighbor, discountsUsed + 1))

        minCost = min(dist[n - 1])
        return -1 if minCost == float("inf") else minCost


n = 5
highways = [[0, 1, 4], [2, 1, 3], [1, 4, 11], [3, 2, 3], [3, 4, 2]]
discounts = 1
print(Solution().minimumCost(n, highways, discounts))
