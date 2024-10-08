# time complexity: O(n+m)
# space complexity: O(n+m)
from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n

        def dfs(currNode):
            if currNode == destination:
                return True
            if not seen[currNode]:
                seen[currNode] = True
                for nextNode in graph[currNode]:
                    if dfs(nextNode):
                        return True
            return False
        return dfs(source)


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
print(Solution().validPath(n, edges, source, destination))
