# time complexity: O(n^3 + Q)
# space complexity: O(n^2)
from collections import defaultdict, deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])
            indegree[edge[1]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        nodePrerequisites = defaultdict(set)

        while q:
            node = q.popleft()

            for adj in adjList[node]:
                nodePrerequisites[adj].add(node)
                for prereq in nodePrerequisites[node]:
                    nodePrerequisites[adj].add(prereq)

                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)

        answer = []
        for q in queries:
            answer.append(q[0] in nodePrerequisites[q[1]])

        return answer


numCourses = 2
prerequisites = [[1, 0]]
queries = [[0, 1], [1, 0]]
print(Solution().checkIfPrerequisite(numCourses, prerequisites, queries))
numCourses = 2
prerequisites = []
queries = [[1, 0], [0, 1]]
print(Solution().checkIfPrerequisite(numCourses, prerequisites, queries))
numCourses = 3
prerequisites = [[1, 2], [1, 0], [2, 0]]
queries = [[1, 0], [1, 2]]
print(Solution().checkIfPrerequisite(numCourses, prerequisites, queries))
