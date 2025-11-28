# time complexity: O(n+m)
# space complexity: O(n+m)
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adjList = [[] for _ in range(n)]
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        componentCount = [0]
        self.dfs(0, -1, adjList, values, k, componentCount)

        return componentCount[0]

    def dfs(self, currNode: int, parentNode: int, adjList: List[List[int]],
            nodeValues: List[int], k: int, componentCount: List[int]) -> int:

        total = 0
        for neighborNode in adjList[currNode]:
            if neighborNode != parentNode:
                total += self.dfs(neighborNode, currNode,
                                  adjList, nodeValues, k, componentCount)
                total %= k
        total += nodeValues[currNode]
        total %= k
        if total == 0:
            componentCount[0] += 1

        return total


n = 5
edges = [[0, 2], [1, 2], [1, 3], [2, 4]]
values = [1, 8, 1, 4, 4]
k = 6
print(Solution().maxKDivisibleComponents(n, edges, values, k))
