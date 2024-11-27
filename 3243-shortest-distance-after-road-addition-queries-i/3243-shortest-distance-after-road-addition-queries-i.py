# time complexity: O(q*(n+q))
# space complexity: O(n+q)
from collections import deque
from typing import List


class Solution:

    def bfs(self, n: int, adj_list: List[List[int]]) -> int:
        visited = [False] * n
        nodeQueue = deque()

        nodeQueue.append(0)
        visited[0] = True

        currentlayerNodeCount = 1
        nextLayerNodeCount = 0

        layersExplored = 0

        while nodeQueue:

            for _ in range(currentlayerNodeCount):
                currentNode = nodeQueue.popleft()

                if currentNode == n - 1:
                    return layersExplored

                for neighbor in adj_list[currentNode]:
                    if visited[neighbor]:
                        continue
                    nodeQueue.append(
                        neighbor
                    )
                    nextLayerNodeCount += (
                        1
                    )
                    visited[neighbor] = True

            currentlayerNodeCount = nextLayerNodeCount
            nextLayerNodeCount = 0
            layersExplored += 1

        return -1

    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        answer = []
        adj_list = [[] for _ in range(n)]

        for i in range(n - 1):
            adj_list[i].append(i + 1)

        for road in queries:
            u, v = road
            adj_list[u].append(v)

            answer.append(self.bfs(n, adj_list))

        return answer


n = 5
queries = [[2, 4], [0, 2], [0, 4]]
print(Solution().shortestDistanceAfterQueries(n, queries))
n = 4
queries = [[0, 3], [0, 2]]
print(Solution().shortestDistanceAfterQueries(n, queries))
