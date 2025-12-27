# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        availableRooms = [i for i in range(n)]
        usedRooms = []
        counter = [0] * n

        for startTime, endTime in meetings:
            while usedRooms and usedRooms[0][0] <= startTime:
                ending, room = heappop(usedRooms)
                heappush(availableRooms, room)
            
            if not availableRooms:
                end, room = heappop(usedRooms)
                endTime = end + (endTime - startTime)
                heappush(availableRooms, room)

            room = heappop(availableRooms)
            heappush(usedRooms, (endTime, room))
            counter[room] += 1


        return counter.index(max(counter))




n = 3
meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
print(Solution().mostBooked(n, meetings))
