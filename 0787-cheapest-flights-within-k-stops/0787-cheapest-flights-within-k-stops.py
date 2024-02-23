# time complexity: O(e*k)
# space complexity: O(n)
from collections import defaultdict
from queue import Queue
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        dist = [float('inf')] * n
        dist[src] = 0

        q = Queue()
        q.put((src, 0))
        stops = 0

        while not q.empty() and stops <= k:
            sz = q.qsize()
            for _ in range(sz):
                node, distance = q.get()

                if node not in adj:
                    continue

                for neighbour, price in adj[node]:
                    if price + distance >= dist[neighbour]:
                        continue
                    dist[neighbour] = price + distance
                    q.put((neighbour, dist[neighbour]))

            stops += 1

        return dist[dst] if dist[dst] != float('inf') else -1


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1

print(Solution().findCheapestPrice(n, flights, src, dst, k))
