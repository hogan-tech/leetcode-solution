# time complexity: O(V+E)
# space complexity: O(V)
from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjList = [[] for _ in range(numCourses)]

        for inNode, outNode in prerequisites:
            adjList[outNode].append(inNode)
            indegree[inNode] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []
        count = 0
        while queue:
            node = queue.popleft()
            result.append(node)
            count += 1
            for neighbor in adjList[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if count != numCourses:
            return []

        return result


numCourses = 2
prerequisites = [[1, 0]]
print(Solution().findOrder(numCourses, prerequisites))
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(Solution().findOrder(numCourses, prerequisites))
numCourses = 1
prerequisites = []
print(Solution().findOrder(numCourses, prerequisites))
numCourses = 6
prerequisites = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]
print(Solution().findOrder(numCourses, prerequisites))
