# time complexity: O(nlogn)
# space complexity: O(n)
import heapq
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        for i in range(len(times)):
            events.append([times[i][0], i])
            events.append([times[i][1], ~i])
        events.sort()
        print(events)
        availableChairs = list(
            range(len(times))
        )

        occupiedChairs = []

        for event in events:
            time, friend = event

            while occupiedChairs and occupiedChairs[0][0] <= time:
                _, chair = heapq.heappop(
                    occupiedChairs
                )
                heapq.heappush(availableChairs, chair)

            if friend >= 0:
                chair = heapq.heappop(availableChairs)
                if friend == targetFriend:
                    return chair
                heapq.heappush(
                    occupiedChairs, [times[friend][1], chair]
                )

        return -1


times = [[1, 4], [2, 3], [4, 6]]
targetFriend = 1
print(Solution().smallestChair(times, targetFriend))
