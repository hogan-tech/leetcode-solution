# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def dfs(self, graph: List[List[int]], visited: List[bool], fromNode: int):
        change = 0
        visited[fromNode] = True
        for toNode in graph[fromNode]:
            if not visited[abs(toNode)]:
                change += self.dfs(graph, visited, abs(toNode)) + \
                    (1 if toNode > 0 else 0)
        return change

    def minReorder(self, n: int, connections: List[List[int]]):
        graph = [[] for _ in range(n)]
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(-c[0])
        visited = [False] * n
        return self.dfs(graph, visited, 0)


n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
print(Solution().minReorder(n, connections))
