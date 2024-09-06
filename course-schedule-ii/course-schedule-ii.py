from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        nodeVisited = 0
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            nodeVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if nodeVisited != numCourses:
            return []
        return result


numCourses = 6
prerequisites = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]


print(Solution().findOrder(numCourses, prerequisites))
