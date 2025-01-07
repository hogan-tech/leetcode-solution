# time complexity: O(r*s)
# space complexity: O(r*s)
from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0
        adjList = defaultdict(set)
        for group, route in enumerate(routes):
            for stop in route:
                adjList[stop].add(group)
        queue = deque()
        queue.append((source, 0))
        visited = set()
        while queue:
            stop, buses = queue.popleft()
            if stop == target:
                return buses
            for group in adjList[stop]:
                for neighbor in routes[group]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, buses + 1))
                routes[group] = []
        return -1


routes = [[1, 2, 7], [3, 6, 7]]
source = 1
target = 6
print(Solution().numBusesToDestination(routes, source, target))
routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
source = 15
target = 12
print(Solution().numBusesToDestination(routes, source, target))
