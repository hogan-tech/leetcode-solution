# time complexity: O(n)
# space complexity: O(n)
from typing import List
from collections import defaultdict


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        reverseGraph = defaultdict(list)

        for startVertex, endVertex in invocations:
            graph[startVertex].append(endVertex)
            reverseGraph[endVertex].append(startVertex)

        suspiciousSet = set()

        def dfs(node):
            if node in suspiciousSet:
                return
            suspiciousSet.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        dfs(k)

        print(graph)
        print(reverseGraph)

        for method in suspiciousSet:
            for invoker in reverseGraph[method]:
                if invoker not in suspiciousSet:
                    return list(range(n))

        return [i for i in range(n) if i not in suspiciousSet]


n = 5
k = 0
invocations = [[1, 2], [0, 2], [0, 1], [3, 4]]
print(Solution().remainingMethods(n, k, invocations))
