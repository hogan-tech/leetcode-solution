# time complexity: O(n^2)
# space complexity: O(n^2)
from collections import deque
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        depth = [0] * (n + 1)
        queue = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        maxDepth = 0
        while queue:
            currNode = queue.popleft()
            for neighbor in graph[currNode]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    depth[neighbor] = depth[currNode] + 1
                    maxDepth = max(maxDepth, depth[neighbor])
                    queue.append(neighbor)
        return pow(2, maxDepth - 1, MOD)


edges = [[1, 2]]
print(Solution().assignEdgeWeights(edges))
edges = [[1, 2], [1, 3], [3, 4], [3, 5]]
print(Solution().assignEdgeWeights(edges))
