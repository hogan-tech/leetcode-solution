# time complexity: O(v+e)
# space complexity: O(v+e)
from collections import deque
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        result = list(range(n))

        for rich in richer:
            graph[rich[0]].append(rich[1])
            indegree[rich[1]] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()

            for neighbor in graph[node]:
                if quiet[result[node]] < quiet[result[neighbor]]:
                    result[neighbor] = result[node]

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return result


richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
quiet = [3, 2, 5, 4, 6, 1, 7, 0]
print(Solution().loudAndRich(richer, quiet))
richer = []
quiet = [0]
print(Solution().loudAndRich(richer, quiet))
