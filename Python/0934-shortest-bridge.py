# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        firstR, firstC = -1, -1

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    firstR, firstC = r, c
                    break

        bfsQueue = [(firstR, firstC)]
        secondBfsQueue = [(firstR, firstC)]
        grid[firstR][firstC] = 2

        while bfsQueue:
            newBfs = []
            for x, y in bfsQueue:
                for curR, curC in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= curR < n and 0 <= curC < n and grid[curR][curC] == 1:
                        newBfs.append((curR, curC))
                        secondBfsQueue.append((curR, curC))
                        grid[curR][curC] = 2
            bfsQueue = newBfs

        distance = 0
        while secondBfsQueue:
            newBfs = []
            for x, y in secondBfsQueue:
                for curR, curC in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= curR < n and 0 <= curC < n:
                        if grid[curR][curC] == 1:
                            return distance
                        elif grid[curR][curC] == 0:
                            newBfs.append((curR, curC))
                            grid[curR][curC] = -1

            secondBfsQueue = newBfs
            distance += 1


grid = [[0, 1], [1, 0]]
print(Solution().shortestBridge(grid))
grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
print(Solution().shortestBridge(grid))
grid = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [
    1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
print(Solution().shortestBridge(grid))
