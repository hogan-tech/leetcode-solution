# time complexity: O(V + E)
# space complexity: O(E)
from collections import defaultdict
from typing import List


class Solution:
    rank = {}
    graph = defaultdict(list)
    connectDict = {}

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.formGraph(n, connections)
        self.dfs(0, 0)
        result = []
        for u, v in self.connectDict:
            result.append([u, v])
        return result

    def dfs(self, node: int, discoveryRank: int) -> int:
        if self.rank[node]:
            return self.rank[node]
        self.rank[node] = discoveryRank
        minRank = discoveryRank + 1
        for neighbor in self.graph[node]:
            if self.rank[neighbor] and self.rank[neighbor] == discoveryRank - 1:
                continue
            recursiveRank = self.dfs(neighbor, discoveryRank + 1)
            if recursiveRank <= discoveryRank:
                del self.connectDict[(
                    min(node, neighbor), max(node, neighbor))]
            minRank = min(minRank, recursiveRank)
        return minRank

    def formGraph(self, n: int, connections: List[List[int]]):
        self.rank = {}
        self.graph = defaultdict(list)
        self.connectDict = {}
        for i in range(n):
            self.rank[i] = None

        for edge in connections:
            u, v = edge[0], edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u)
            self.connectDict[(min(u, v), max(u, v))] = 1


n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(Solution().criticalConnections(n, connections))
n = 2
connections = [[0, 1]]
print(Solution().criticalConnections(n, connections))
