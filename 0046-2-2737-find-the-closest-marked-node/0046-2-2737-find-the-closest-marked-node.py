# time complexity: O((n+m)logn)
# space complexity: O(n + m)
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        markedSet = set(marked)
        adjList = defaultdict(list)
        for inNode, outNode, weight in edges:
            adjList[inNode].append([outNode, weight])

        pq = []
        dist = defaultdict(lambda: float('inf'))
        dist[s] = 0
        heappush(pq, [0, s])

        while pq:
            currWeight, currNode = heappop(pq)
            if currNode in markedSet:
                return dist[currNode]

            for nextNode, weight in adjList[currNode]:
                nextWeight = weight + currWeight

                if nextWeight < dist[nextNode]:
                    dist[nextNode] = nextWeight
                    heappush(pq, [nextWeight, nextNode])

        return -1


n = 3
edges = [[0, 2, 3], [0, 1, 2], [0, 2, 9], [2, 0, 6], [0, 2, 9], [1, 0, 8], [0, 2, 5], [0, 1, 6], [0, 2, 10], [
    2, 0, 1], [1, 0, 1], [0, 1, 5], [0, 2, 1], [2, 0, 10], [1, 0, 6], [1, 0, 4], [2, 1, 2], [1, 0, 1], [2, 1, 8]]
s = 1
marked = [2]
print(Solution().minimumDistance(n, edges, s, marked))

n = 3
edges = [[0, 1, 1], [0, 1, 3], [1, 2, 1], [0, 2, 8], [1, 2, 1], [0, 1, 2], [1, 2, 7], [
    0, 1, 4], [1, 0, 9], [0, 1, 2], [0, 1, 4], [2, 1, 2], [0, 2, 4], [1, 0, 10], [1, 2, 7]]
s = 2
marked = [1]
print(Solution().minimumDistance(n, edges, s, marked))
n = 4
edges = [[0, 1, 1], [1, 2, 3], [2, 3, 2], [0, 3, 4]]
s = 0
marked = [2, 3]
print(Solution().minimumDistance(n, edges, s, marked))
n = 5
edges = [[0, 1, 2], [0, 2, 4], [1, 3, 1], [2, 3, 3], [3, 4, 2]]
s = 1
marked = [0, 4]
print(Solution().minimumDistance(n, edges, s, marked))
n = 4
edges = [[0, 1, 1], [1, 2, 3], [2, 3, 2]]
s = 3
marked = [0, 1]
print(Solution().minimumDistance(n, edges, s, marked))
n = 2
edges = [[0, 1, 1], [0, 1, 2], [0, 1, 3], [1, 0, 8], [1, 0, 10], [0, 1, 7], [
    0, 1, 2], [0, 1, 6], [1, 0, 1], [1, 0, 2], [1, 0, 4], [0, 1, 9], [1, 0, 10]]
s = 0
marked = [1]
print(Solution().minimumDistance(n, edges, s, marked))
