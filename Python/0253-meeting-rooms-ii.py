# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        minHp = []
        intervals.sort()
        heappush(minHp, intervals[0][1])
        for start, end in intervals[1:]:
            if minHp[0] <= start:
                heappop(minHp)
            heappush(minHp, end)

        return len(minHp)


intervals = [[7, 10], [2, 4]]
print(Solution().minMeetingRooms(intervals))
intervals = [[0, 30], [5, 10], [15, 20]]
print(Solution().minMeetingRooms(intervals))
intervals = [[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]]
print(Solution().minMeetingRooms(intervals))
