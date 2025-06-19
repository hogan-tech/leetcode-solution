# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict, deque
from typing import List

# Union Find
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]
    
    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]
        return node
    
    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return False

        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
            self.rank[parent1] += 1
        else:
            self.parent[parent1] = parent2 
            self.rank[parent2] += 1
        
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
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
