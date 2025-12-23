# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        result = 0
        maxVal = 0
        for event in events:
            while pq and pq[0][0] < event[0]:
                maxVal = max(maxVal, pq[0][1])
                heappop(pq)
            result = max(result, maxVal + event[2])
            heappush(pq, (event[1], event[2]))

        return result


events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
print(Solution().maxTwoEvents(events))
events = [[1, 3, 2], [4, 5, 2], [1, 5, 5]]
print(Solution().maxTwoEvents(events))
events = [[1, 5, 3], [1, 5, 1], [6, 6, 5]]
print(Solution().maxTwoEvents(events))
