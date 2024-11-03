# time complexity: O(n*m)
# space complexity: O(n*m)
import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ROW = len(moveTime)
        COL = len(moveTime[0])
        heap = [(0, 0, 0)]
        visited = [[float('inf')] * COL for _ in range(ROW)]
        visited[0][0] = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            time, currR, currC = heapq.heappop(heap)
            if currR == ROW - 1 and currC == COL - 1:
                return time

            for dR, dC in directions:
                nR, nC = currR + dR, currC + dC
                if 0 <= nR < ROW and 0 <= nC < COL:
                    nextTime = max(time + 1, moveTime[nR][nC] + 1)
                    if nextTime < visited[nR][nC]:
                        visited[nR][nC] = nextTime
                        heapq.heappush(heap, (nextTime, nR, nC))
        return -1


moveTime = [[0, 4], [4, 4]]
print(Solution().minTimeToReach(moveTime))  # Output: 6

moveTime = [[0, 0, 0], [0, 0, 0]]
print(Solution().minTimeToReach(moveTime))  # Output: 3

moveTime = [[0, 1], [1, 2]]
print(Solution().minTimeToReach(moveTime))  # Output: 3
