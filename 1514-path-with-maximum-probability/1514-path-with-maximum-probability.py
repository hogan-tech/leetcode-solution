# time complexity: O(n*m)
# space complexity: O(n)
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        maxProb = [0] * n
        maxProb[start] = 1

        for i in range(n - 1):
            hasUpdate = 0
            for j in range(len(edges)):
                u, v = edges[j]
                pathProb = succProb[j]
                if maxProb[u] * pathProb > maxProb[v]:
                    maxProb[v] = maxProb[u] * pathProb
                    hasUpdate = 1
                if maxProb[v] * pathProb > maxProb[u]:
                    maxProb[u] = maxProb[v] * pathProb
                    hasUpdate = 1
            if not hasUpdate:
                break

        return maxProb[end]


n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2
print(Solution().maxProbability(n, edges, succProb, start, end))
