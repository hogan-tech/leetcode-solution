# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adjacencyList = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adjacencyList[i].append(j)
                    adjacencyList[j].append(i)
        numOfConnectedComponents = 0
        visited = [False] * n

        def dfs(stone):
            visited[stone] = True
            for neighbor in adjacencyList[stone]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                numOfConnectedComponents += 1

        return n - numOfConnectedComponents


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
print(Solution().removeStones(stones))
