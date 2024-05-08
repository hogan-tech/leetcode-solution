# time complexity: O(n^2logn)
# space complexity: O(n)
import collections
import heapq
from typing import List


class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = collections.defaultdict(list)
        for s, e, v in roads:
            graph[s].append((e, v * (1+k)))
            graph[e].append((s, v * (1+k)))
        ans = []

        def dijkstra(node):
            nonlocal graph, visited
            heap = [(0, node, 0)]
            res = appleCost[node-1]
            while heap:
                cur_val, cur_node, bought = heapq.heappop(heap)
                if bought:
                    res = min(res, cur_val)
                    break
                if cur_node in visited:
                    continue
                visited.add(cur_node)
                for nei, cost in graph[cur_node]:
                    heapq.heappush(heap, (cur_val + cost, nei, 0))
                    heapq.heappush(heap,
                                   (cur_val + cost + appleCost[nei-1], nei, 1))
            return res
        for i in range(1, n+1):
            visited = set()
            ans.append(dijkstra(i))
        return ans


n = 4
roads = [[1, 2, 4], [2, 3, 2], [2, 4, 5], [3, 4, 1], [1, 3, 4]]
appleCost = [56, 42, 102, 301]
k = 2
print(Solution().minCost(n, roads, appleCost, k))
