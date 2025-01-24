# time complexity: O(m + n)
# space complexity: O(m + n)
from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adj = [[] for _ in range(n)]
        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        queue = deque()
        safe = [False] * n
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            safe[node] = True
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        result = []
        for i in range(n):
            if safe[i]:
                result.append(i)
        return result


graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
print(Solution().eventualSafeNodes(graph))
graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
print(Solution().eventualSafeNodes(graph))
