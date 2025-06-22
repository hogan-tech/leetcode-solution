# time complexity: O(n)
# space complexity: O(n)
from functools import lru_cache
from typing import List
from collections import defaultdict


class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        @lru_cache(None)
        def dfs(node, parent):
            if not adjList[node] or (len(adjList[node]) == 1 and adjList[node][0] == parent):
                return cost[node], 0

            maxSubSum = 0
            totalIncrease = 0
            childScore = []

            for nextNode in adjList[node]:
                if nextNode == parent:
                    continue
                subSum, increases = dfs(nextNode, node)
                childScore.append(subSum)
                maxSubSum = max(maxSubSum, subSum)
                totalIncrease += increases

            for score in childScore:
                if score < maxSubSum:
                    totalIncrease += 1

            return cost[node] + maxSubSum, totalIncrease

        _, result = dfs(0, -1)
        return result


n = 3
edges = [[0, 1], [0, 2]]
cost = [2, 1, 3]
print(Solution().minIncrease(n, edges, cost))
n = 3
edges = [[0, 1], [1, 2]]
cost = [5, 1, 4]
print(Solution().minIncrease(n, edges, cost))
n = 5
edges = [[0, 4], [0, 1], [1, 2], [1, 3]]
cost = [3, 4, 1, 1, 7]
print(Solution().minIncrease(n, edges, cost))
