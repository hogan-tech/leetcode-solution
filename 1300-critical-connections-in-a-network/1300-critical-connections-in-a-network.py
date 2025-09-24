# time complexity: O(V + E)
# space complexity: O(E)
from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        rank = {i: None for i in range(n)}
        graph = defaultdict(list)
        connectDict = {}

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            connectDict[(min(u, v), max(u, v))] = 1

        def dfs(node: int, discoveryRank: int) -> int:
            if rank[node] is not None:
                return rank[node]

            rank[node] = discoveryRank
            minRank = discoveryRank + 1

            for neighbor in graph[node]:
                if rank[neighbor] is not None and rank[neighbor] == discoveryRank - 1:
                    continue
                recursiveRank = dfs(neighbor, discoveryRank + 1)
                if recursiveRank <= discoveryRank:
                    connectDict.pop(
                        (min(node, neighbor), max(node, neighbor)), None)
                minRank = min(minRank, recursiveRank)

            return minRank

        dfs(0, 0)

        return [[u, v] for u, v in connectDict]


n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(Solution().criticalConnections(n, connections))
n = 2
connections = [[0, 1]]
print(Solution().criticalConnections(n, connections))
