# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        i = 0
        n = len(stations)
        maxHeap = []
        maxDistance = startFuel
        stops = 0
        while maxDistance < target:
            if i < n and stations[i][0] <= maxDistance:
                heappush(maxHeap, -stations[i][1])
                i += 1
            elif not maxHeap:
                return -1
            else:
                maxDistance += -heappop(maxHeap)
                stops += 1

        return stops


target = 1
startFuel = 1
stations = []
print(Solution().minRefuelStops(target, startFuel, stations))
target = 100
startFuel = 1
stations = [[10, 100]]
print(Solution().minRefuelStops(target, startFuel, stations))
target = 100
startFuel = 10
stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
print(Solution().minRefuelStops(target, startFuel, stations))
