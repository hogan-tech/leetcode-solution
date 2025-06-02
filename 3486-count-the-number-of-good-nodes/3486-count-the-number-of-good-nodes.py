# time complexity: O(v+e)
# space complexity: O(v+e)
from collections import defaultdict
from typing import List


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        def dfs(currNode: int, parent: int):
            size = 1
            for neighbor in adjList[currNode]:
                if neighbor != parent:
                    size += dfs(neighbor, currNode)
            subtreeSize[currNode] = size
            return size

        adjList = defaultdict(list)
        n = len(edges) + 1
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        subtreeSize = [0 for _ in range(n)]

        dfs(0, -1)
        result = 0
        for currNode in range(n):
            prevSize = -1
            goodNode = True
            for neighbor in adjList[currNode]:
                if subtreeSize[neighbor] < subtreeSize[currNode]:
                    if prevSize == -1:
                        prevSize = subtreeSize[neighbor]
                    elif prevSize != subtreeSize[neighbor]:
                        goodNode = False
                        break
            if goodNode:
                result += 1

        return result


edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
print(Solution().countGoodNodes(edges))
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [1, 6], [2, 7], [3, 8]]
print(Solution().countGoodNodes(edges))
edges = [[0, 1], [1, 2], [1, 3], [1, 4], [0, 5], [5, 6],
         [6, 7], [7, 8], [0, 9], [9, 10], [9, 12], [10, 11]]
print(Solution().countGoodNodes(edges))
