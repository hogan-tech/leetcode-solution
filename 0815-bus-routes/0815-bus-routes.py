from collections import defaultdict
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0
        adjList = defaultdict(set)
        for group, route in enumerate(routes):
            for stop in route:
                adjList[stop].add(group)
        queue = [(source, 0)]
        visited = set()
        for stop, buses in queue:
            if stop == target:
                return buses
            for group in adjList[stop]:
                for nei in routes[group]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, buses + 1))
                routes[group] = []
        return -1


routes = [[1, 2, 7], [3, 6, 7]]
source = 1
target = 6


print(Solution().numBusesToDestination(routes, source, target))
