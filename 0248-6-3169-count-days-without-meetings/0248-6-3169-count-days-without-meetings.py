# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev = meetings[0]
        mergeList = [prev]
        for i in range(1, len(meetings)):
            currMeeting = meetings[i]
            if prev[1] >= currMeeting[0]:
                if prev[1] >= currMeeting[1]:
                    continue
                else:
                    prev[1] = currMeeting[1]
            else:
                mergeList.append(currMeeting)
            prev = mergeList[-1]

        for start, end in mergeList:
            days -= (end - start + 1)

        return days


days = 34
meetings = [[15, 34], [5, 18], [9, 20], [1, 4],
            [6, 30], [6, 28], [25, 30], [23, 24]]
print(Solution().countDays(days, meetings))
days = 10
meetings = [[5, 7], [1, 3], [9, 10]]
print(Solution().countDays(days, meetings))
days = 5
meetings = [[2, 4], [1, 3]]
print(Solution().countDays(days, meetings))
days = 6
meetings = [[1, 6]]
print(Solution().countDays(days, meetings))
