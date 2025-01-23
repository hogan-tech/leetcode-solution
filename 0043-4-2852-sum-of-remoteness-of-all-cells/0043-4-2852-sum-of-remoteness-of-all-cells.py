# time complexity: O(m*n)
# space complexity: O(m*n)
from collections import deque
from typing import List


class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        def bfs(grid, row, col, totalSum):
            queue = deque()
            currSum = grid[row][col]
            currSize = 1
            grid[row][col] = -1

            queue.append((row, col))
            while queue:
                currR, currC = queue.popleft()
                for dR, dC in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nextR = currR + dR
                    nextC = currC + dC
                    if 0 <= nextR < ROW and 0 <= nextC < COL and grid[nextR][nextC] > 0:
                        queue.append((nextR, nextC))
                        currSum += grid[nextR][nextC]
                        currSize += 1
                        grid[nextR][nextC] = -1

            return (totalSum - currSum) * currSize

        ROW = len(grid)
        COL = len(grid[0])
        totalSum = sum(val for row in grid for val in row if val != -1)
        result = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] > 0:
                    result += bfs(grid, r, c, totalSum)
        return result


grid = [[-1, 1, -1], [5, -1, 4], [-1, 3, -1]]
print(Solution().sumRemoteness(grid))
grid = [[-1, 3, 4], [-1, -1, -1], [3, -1, -1]]
print(Solution().sumRemoteness(grid))
grid = [[1]]
print(Solution().sumRemoteness(grid))
