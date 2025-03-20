# time complexity: O(n+e+q)
# space complexity: O(n)
from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = list(range(n))

        minPathCost = [-1] * n

        def findRoot(node: int) -> int:
            if parent[node] != node:
                parent[node] = findRoot(parent[node])
            return parent[node]

        for source, target, weight in edges:
            sourceRoot = findRoot(source)
            targetRoot = findRoot(target)

            minPathCost[targetRoot] &= weight

            if sourceRoot != targetRoot:
                minPathCost[targetRoot] &= minPathCost[sourceRoot]
                parent[sourceRoot] = targetRoot

        result = []
        for start, end in query:
            if start == end:
                result.append(0)
            elif findRoot(start) != findRoot(end):
                result.append(-1)
            else:
                result.append(minPathCost[findRoot(start)])

        return result


n = 5
edges = [[0, 1, 7], [1, 3, 7], [1, 2, 1]]
query = [[0, 3], [3, 4]]
print(Solution().minimumCost(n, edges, query))
n = 3
edges = [[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]]
query = [[1, 2]]
print(Solution().minimumCost(n, edges, query))
