# time complexity: O(nlogn)
# space complexity: O(n)
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        freeRooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(freeRooms, intervals[0][1])
        for i in intervals[1:]:
            if freeRooms[0] <= i[0]:
                heapq.heappop(freeRooms)
            heapq.heappush(freeRooms, i[1])
        return len(freeRooms)


intervals = [[7, 10], [2, 4]]
print(Solution().minMeetingRooms(intervals))
