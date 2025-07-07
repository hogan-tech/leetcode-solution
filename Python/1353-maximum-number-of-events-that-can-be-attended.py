# time complexity: O((t + n)logn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        maxDay = max(event[1] for event in events)
        events.sort()
        hp = []
        result, left = 0, 0
        for right in range(1, maxDay + 1):
            while left < n and events[left][0] <= right:
                heappush(hp, events[left][1])
                left += 1
            while hp and hp[0] < right:
                heappop(hp)
            if hp:
                heappop(hp)
                result += 1

        return result


events = [[1, 2], [2, 3], [3, 4]]
print(Solution().maxEvents(events))
events = [[1, 2], [2, 3], [3, 4], [1, 2]]
print(Solution().maxEvents(events))
