# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict, deque
from typing import List

# Union Find
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = list(range(n))

    def find(self, node: int) -> int:
        while node != self.parents[node]:
            node = self.parents[node]
        return node

    def union(self, nodeX: int, nodeY: int) -> bool:
        parentX, parentY = self.find(nodeX), self.find(nodeY)
        if parentX == parentY:
            return False
        self.parents[parentX] = parentY
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        disjointUnionSet = UnionFind(n)
        for startVertex, endVertex in edges:
            if not disjointUnionSet.union(startVertex, endVertex):
                return False
        return True

# BFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adjList = defaultdict(list)
        seen = set()
        queue = deque()

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        seen.add(0)
        queue.append(0)
        while queue:
            node = queue.popleft()
            for neighbor in adjList[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return len(seen) == n

# DFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adjList = [[] for _ in range(n)]
        seen = {0}
        stack = [0]

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        while stack:
            node = stack.pop()
            for neighbor in adjList[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

        return len(seen) == n


n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(Solution().validTree(n, edges))
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(Solution().validTree(n, edges))
