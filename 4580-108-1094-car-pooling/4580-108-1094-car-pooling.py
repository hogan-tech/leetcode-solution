# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        fromHp = []
        toHp = []
        for num, fromTrip, toTrip in trips:
            heappush(fromHp, [fromTrip, -num])
            heappush(toHp, [toTrip, num])

        while fromHp and toHp:
            minFrom = fromHp[0]
            minTo = toHp[0]
            if minFrom[0] < minTo[0]:
                _, val = heappop(fromHp)
                capacity += val
                if capacity < 0:
                    return False
            else:
                _, val = heappop(toHp)
                capacity += val

        return True


'''
   2     3
   1     5
         5    7
'''

trips = [[2, 1, 5], [3, 5, 7]]
capacity = 3
print(Solution().carPooling(trips, capacity))
trips = [[2, 1, 5], [3, 3, 7]]
capacity = 5
print(Solution().carPooling(trips, capacity))
