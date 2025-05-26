# time complexity: O(n + m)
# space complexity: O(n + m)
from typing import List
from collections import deque


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        indegrees = [0] * n
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            indegrees[edge[1]] += 1
        zeroIndegree = deque()
        for i in range(n):
            if indegrees[i] == 0:
                zeroIndegree.append(i)
        counts = [[0]*26 for _ in range(n)]
        for i in range(n):
            counts[i][ord(colors[i]) - ord('a')] += 1
        maxCount = 0
        visited = 0
        while zeroIndegree:
            u = zeroIndegree.popleft()
            visited += 1
            for v in graph[u]:
                for i in range(26):
                    counts[v][i] = max(counts[v][i],
                                       counts[u][i] + (ord(colors[v]) - ord('a') == i))
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    zeroIndegree.append(v)
            maxCount = max(maxCount, max(counts[u]))
        return maxCount if visited == n else -1


colors = "abaca"
edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
print(Solution().largestPathValue(colors, edges))
colors = "a"
edges = [[0, 0]]
print(Solution().largestPathValue(colors, edges))
