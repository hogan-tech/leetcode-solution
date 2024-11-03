# time complexity: O(n*m)
# space complexity: O(n*m)
import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ROW = len(moveTime)
        COL = len(moveTime[0])
        heap = [(0, 0, 0, True)]
        visited = [[float('inf')] * COL for _ in range(ROW)]
        visited[0][0] = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            time, currR, currC, currOddCount = heapq.heappop(heap)
            if currR == ROW - 1 and currC == COL - 1:
                print((time, currR, currC))
                return time
            for dR, dC in directions:
                nR, nC = currR + dR, currC + dC
                if 0 <= nR < ROW and 0 <= nC < COL:
                    nextTime = max(time, moveTime[nR][nC]) + (1 if currOddCount else 2)
                    if nextTime < visited[nR][nC]:
                        visited[nR][nC] = nextTime
                        heapq.heappush(heap, (nextTime, nR, nC, not currOddCount))
        return -1


moveTime = [[0, 4], [4, 4]]
print(Solution().minTimeToReach(moveTime))  # Output: 7

moveTime = [[0,0,0,0],[0,0,0,0]]
print(Solution().minTimeToReach(moveTime))  # Output: 6

moveTime = [[0, 1], [1, 2]]
print(Solution().minTimeToReach(moveTime))  # Output: 4
