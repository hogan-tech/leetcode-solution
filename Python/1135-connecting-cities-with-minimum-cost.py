# time complexity: O(nlogn)
# space complexity: O(n^2)
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v, cost in connections:
            adjList[u].append((cost, v))
            adjList[v].append((cost, u))

        minHp = [(0, 1)]
        visited = set()
        totalCost = 0
        while minHp:
            currCost, currNode = heappop(minHp)
            if currNode in visited:
                continue
            visited.add(currNode)
            totalCost += currCost
            if len(visited) == n:
                return totalCost
            for nextCost, nextNode in adjList[currNode]:
                if nextNode not in visited:
                    heappush(minHp, (nextCost, nextNode))

        return -1


n = 3
connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
print(Solution().minimumCost(n, connections))
n = 4
connections = [[1, 2, 3], [3, 4, 4]]
print(Solution().minimumCost(n, connections))
