# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        startHeap = []
        endHeap = []
        result = [-1] * len(intervals)

        for i, (startTime, endTime) in enumerate(intervals):
            heappush(startHeap, (startTime, i))
            heappush(endHeap, (endTime, i))

        while endHeap:
            currEnd, currEndIdx = heappop(endHeap)
            while startHeap and startHeap[0][0] < currEnd:
                heappop(startHeap)

            if startHeap:
                result[currEndIdx] = startHeap[0][1]

        return result


intervals = [[1, 2]]
print(Solution().findRightInterval(intervals))
intervals = [[3, 4], [2, 3], [1, 2]]
print(Solution().findRightInterval(intervals))
intervals = [[1, 4], [2, 3], [3, 4]]
print(Solution().findRightInterval(intervals))
