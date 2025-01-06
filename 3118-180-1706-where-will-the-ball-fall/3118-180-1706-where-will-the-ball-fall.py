# time complexity: O(m*n)
# space complexity: O(1)
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ROW = len(grid)
        COL = len(grid[0])
        result = [-1] * COL

        for c in range(COL):
            currC = c
            for r in range(ROW):
                nextC = currC + grid[r][currC]
                if nextC < 0 or nextC > COL - 1 or grid[r][currC] != grid[r][nextC]:
                    break
                if r == ROW - 1:
                    result[c] = nextC
                currC = nextC
        return result

grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1],
        [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]
print(Solution().findBall(grid))
grid = [[-1]]
print(Solution().findBall(grid))
grid = [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1],
        [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]
print(Solution().findBall(grid))
