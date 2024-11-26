from collections import defaultdict
from typing import List




class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = defaultdict(int)
        for i in range(n):
            indegree[i] = 0
        for edge in edges:
            indegree[edge[1]] += 1
        
        champion = -1
        championCount = 0
        for key, count in indegree.items():
            if count == 0:
                champion =  key
                championCount += 1
            
        print(indegree)
        return champion if championCount == 1 else -1
        


n = 3
edges = [[0, 1], [1, 2]]
print(Solution().findChampion(n, edges))
n = 4
edges = [[0, 2], [1, 3], [1, 2]]
print(Solution().findChampion(n, edges))
n = 3
edges = [[0, 1], [2, 1]]
print(Solution().findChampion(n, edges))
n = 1
edges = [[2, 1]]
print(Solution().findChampion(n, edges))
n = 2
edges = []
print(Solution().findChampion(n, edges))
n = 3
edges = [[0,1]]
print(Solution().findChampion(n, edges))
