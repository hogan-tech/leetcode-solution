# time complexity: O(n^2)
# space complexity: O(n)
from collections import defaultdict, deque
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adjList = defaultdict(list)
        visited = [False] * n
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        for restrictedNode in restricted:
            visited[restrictedNode] = True

        queue = deque()
        queue.append(0)
        visited[0] = True
        result = 0
        while queue:
            currNode = queue.popleft()
            result += 1
            for nextNode in adjList[currNode]:
                if not visited[nextNode]:
                    queue.append(nextNode)
                    visited[nextNode] = True

        return result


n = 7
edges = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]]
restricted = [4, 5]
print(Solution().reachableNodes(n, edges, restricted))
n = 7
edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
restricted = [4, 2, 1]
print(Solution().reachableNodes(n, edges, restricted))
