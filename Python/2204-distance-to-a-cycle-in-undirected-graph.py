# time complexity: O(n+e)
# space complexity: O(n+e)
from collections import deque
from typing import List


class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        isInCycle = [True] * n
        visited = [False] * n
        degree = [0] * n
        distances = [0] * n
        adjacencyList = [[] for _ in range(n)]

        for edge in edges:
            adjacencyList[edge[0]].append(edge[1])
            adjacencyList[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1

        nodeQueue = deque()

        for i in range(len(degree)):
            if degree[i] == 1:
                nodeQueue.append(i)

        while nodeQueue:
            currNode = nodeQueue.popleft()
            isInCycle[currNode] = False
            for neighbor in adjacencyList[currNode]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    nodeQueue.append(neighbor)

        for currNode in range(n):
            if isInCycle[currNode]:
                nodeQueue.append(currNode)
                visited[currNode] = True

        currDistance = 0

        while nodeQueue:
            for _ in range(len(nodeQueue)):
                currNode = nodeQueue.popleft()
                distances[currNode] = currDistance
                for neighbor in adjacencyList[currNode]:
                    if visited[neighbor]:
                        continue
                    nodeQueue.append(neighbor)
                    visited[neighbor] = True
            currDistance += 1

        return distances


n = 7
edges = [[1, 2], [2, 4], [4, 3], [3, 1], [0, 1], [5, 2], [6, 5]]
print(Solution().distanceToCycle(n, edges))
