# time complexity: O(n * logn)
# space complexity: O(n^2)
# Dijkstra
from heapq import heappop, heappush
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        seen.add((0, 0))
        priorityQueue = [(grid[0][0], (0, 0))]
        while priorityQueue:
            currVal, (currR, currC) = heappop(priorityQueue)
            if (currR, currC) == (ROW - 1, COL-1):
                return currVal
            for dirR, dirC in directions:
                nextR = currR + dirR
                nextC = currC + dirC
                if 0 <= nextR < ROW and 0 <= nextC < COL and (nextR, nextC) not in seen:
                    seen.add((nextR, nextC))
                    heappush(
                        priorityQueue, (max(currVal, grid[nextR][nextC]), (nextR, nextC)))
        return 0


grid = [[0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6]]
print(Solution().swimInWater(grid))
