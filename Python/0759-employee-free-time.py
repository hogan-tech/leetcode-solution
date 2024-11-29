# time complexity: O(nlogn)
# space complexity: O(n)
import heapq
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        freeTimeList = []
        minStartHeap = []

        for empIdx, empSchedule in enumerate(schedule):
            heapq.heappush(minStartHeap, (empSchedule[0].start, empIdx, 0))

        _, empIdx, eventIdx = minStartHeap[0]
        prevEnd = schedule[empIdx][eventIdx].end

        while minStartHeap:
            startTime, empIdx, eventIdx = heapq.heappop(minStartHeap)

            if eventIdx + 1 < len(schedule[empIdx]):
                heapq.heappush(
                    minStartHeap, (schedule[empIdx][eventIdx+1].start, empIdx, eventIdx+1))

            if prevEnd < startTime:
                freeTimeList.append(Interval(start=prevEnd, end=startTime))

            prevEnd = max(prevEnd, schedule[empIdx][eventIdx].end)

        return freeTimeList


schedule = [
    [Interval(1, 2), Interval(5, 6)],
    [Interval(1, 3)], [Interval(4, 10)]
]
print(Solution().employeeFreeTime(schedule))
