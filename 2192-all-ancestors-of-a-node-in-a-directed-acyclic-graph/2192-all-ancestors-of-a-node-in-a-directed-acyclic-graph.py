# time complexity: O(n^2 + n*m)
# space complexity: O(n+m)
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjacencyList = [[] for _ in range(n)]

        for edge in edges:
            fromNode, toNode = edge
            adjacencyList[toNode].append(fromNode)

        ancestorsList = []

        for i in range(n):
            ancestors = []
            visited = set()
            self.findChildren(i, adjacencyList, visited)
            for node in range(n):
                if node == i:
                    continue
                if node in visited:
                    ancestors.append(node)
            ancestorsList.append(ancestors)

        return ancestorsList

    def findChildren(self, currentNode, adjacencyList, visitedNodes):
        visitedNodes.add(currentNode)

        for neighbour in adjacencyList[currentNode]:
            if neighbour not in visitedNodes:
                self.findChildren(neighbour, adjacencyList, visitedNodes)


n = 8
edgeList = [[0, 3], [0, 4], [1, 3], [2, 4],
            [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
print(Solution().getAncestors(n, edgeList))
