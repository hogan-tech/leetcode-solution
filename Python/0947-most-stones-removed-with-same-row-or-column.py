# time complexity: O(n)
# space complexity: O(n)
from typing import List


class UnionFind:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    def find(self, coordinate):
        if coordinate != self.parents[coordinate]:
            self.parents[coordinate] = self.find(self.parents[coordinate])
        return self.parents[coordinate]

    def union(self, x, y):
        self.parents.setdefault(x, x)
        self.parents.setdefault(y, y)

        self.ranks.setdefault(x, 0)
        self.ranks.setdefault(y, 0)

        if self.ranks[x] > self.ranks[y]:
            self.parents[self.find(y)] = self.find(x)
        elif self.ranks[x] < self.ranks[y]:
            self.parents[self.find(x)] = self.find(y)
        else:
            self.parents[self.find(x)] = self.find(y)
            self.ranks[y] += 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        offset = 100000
        unionFind = UnionFind()
        for x, y in stones:
            unionFind.union(x, (y + offset))
        groups = set()
        for i in unionFind.parents:
            groups.add(unionFind.find(i))

        return len(stones) - len(groups)

# time complexity: O(n^2)
# space complexity: O(n^2)


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
stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
print(Solution().removeStones(stones))
stones = [[0, 0]]
print(Solution().removeStones(stones))
