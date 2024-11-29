# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        freeRooms = []
        for i in range(len(intervals)):
            if freeRooms and freeRooms[0] < intervals[i][0]:
                heappop(freeRooms)
            heappush(freeRooms, intervals[i][1])
        return len(freeRooms)


intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
print(Solution().minGroups(intervals))
