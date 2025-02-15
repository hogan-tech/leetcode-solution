# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        oneIdx = []
        betweenDis = -float('inf')
        for i, seat in enumerate(seats):
            if seat == 1:
                oneIdx.append(i)
        for i in range(1, len(oneIdx)):
            distance = (oneIdx[i] - oneIdx[i - 1]) // 2
            betweenDis = max(distance, betweenDis)

        firstDis = oneIdx[0] - 0
        lastDis = len(seats) - 1 - oneIdx[-1]
        return max(betweenDis, firstDis, lastDis)


'''
two cases
1: between two one index
2: set first is one or last is one

get whole one index:
    calculate between two index
set first or last index:
    calculate first and last distance
return max
'''

seats = [1, 0, 0, 0, 1, 0, 1]
print(Solution().maxDistToClosest(seats))
seats = [1, 0, 0, 0]
print(Solution().maxDistToClosest(seats))
seats = [0, 1]
print(Solution().maxDistToClosest(seats))
seats = [0, 0, 0, 1]
print(Solution().maxDistToClosest(seats))
