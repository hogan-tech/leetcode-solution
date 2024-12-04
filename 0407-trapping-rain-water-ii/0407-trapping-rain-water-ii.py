# time complexity: O(m*n)
# space complexity: O(m*n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        ROW, COL = len(heightMap), len(heightMap[0])
        if ROW < 3 or COL < 3:
            return 0

        heap = []
        for r in range(ROW):
            for c in range(COL):
                if r == 0 or r == ROW - 1 or c == 0 or c == COL - 1:
                    heappush(heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1

        level, result = 0, 0
        while heap:
            currHeight, currR, currC = heappop(heap)
            level = max(currHeight, level)

            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL and heightMap[nextR][nextC] != -1:
                    heappush(heap, (heightMap[nextR][nextC], nextR, nextC))

                    if heightMap[nextR][nextC] < level:
                        result += level - heightMap[nextR][nextC]

                    heightMap[nextR][nextC] = -1

        return result


heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
print(Solution().trapRainWater(heightMap))
heightMap = [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [
    3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]
print(Solution().trapRainWater(heightMap))
