# time complexity: O(nlogn)
# space complexity: O(n)
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        freeRooms = []
        intervals.sort()
        heapq.heappush(freeRooms, intervals[0][1])
        for interval in intervals[1:]:
            if freeRooms[0] <= interval[0]:
                heapq.heappop(freeRooms)
            heapq.heappush(freeRooms, interval[1])

        return len(freeRooms)


intervals = [[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]]
print(Solution().minMeetingRooms(intervals))
