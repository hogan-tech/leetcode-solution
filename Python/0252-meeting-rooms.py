# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        prevEnd = intervals[0][1]
        for currInterval in intervals[1:]:
            if prevEnd > currInterval[0]:
                return False
            prevEnd = currInterval[1]
        return True


intervals = [[0, 30], [5, 10], [15, 20]]
print(Solution().canAttendMeetings(intervals))
intervals = [[7, 10], [2, 4]]
print(Solution().canAttendMeetings(intervals))
