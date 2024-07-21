# time complexity: O(max(k*k,n))
# space complexity: O(max(k*k,n))
from collections import defaultdict
from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        orderRows = self.topoSort(rowConditions, k)
        orderColumns = self.topoSort(colConditions, k)

        if not orderRows or not orderColumns:
            return []
        matrix = [[0] * k for _ in range(k)]
        posRow = {num: i for i, num in enumerate(orderRows)}
        posCol = {num: i for i, num in enumerate(orderColumns)}

        for num in range(1, k + 1):
            if num in posRow and num in posCol:
                matrix[posRow[num]][posCol[num]] = num
        return matrix

    def dfs(self, node: int, adj: defaultdict, visited: List[int], order: List[int], hasCycle: List[bool]):
        visited[node] = 1
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                self.dfs(neighbor, adj, visited, order, hasCycle)
                if hasCycle[0]:
                    return
            elif visited[neighbor] == 1:
                hasCycle[0] = True
                return
        visited[node] = 2
        order.append(node)

    def topoSort(self, edges: List[List[int]], n: int) -> List[int]:
        adj = defaultdict(list)
        order = []
        visited = [0] * (n + 1)
        hasCycle = [False]

        for x, y in edges:
            adj[x].append(y)

        for i in range(1, n + 1):
            if visited[i] == 0:
                self.dfs(i, adj, visited, order, hasCycle)

                if hasCycle[0]:
                    return []

        order.reverse()
        return order


k = 3
rowConditions = [[1, 2], [3, 2]]
colConditions = [[2, 1], [3, 2]]
print(Solution().buildMatrix(k, rowConditions, colConditions))
