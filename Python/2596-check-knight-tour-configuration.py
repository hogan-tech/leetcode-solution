# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)]

        ROW = len(grid)
        COL = len(grid[0])

        def validMove(currR, currC):
            if grid[currR][currC] == (ROW * COL - 1):
                return True
            for dR, dC in dirs:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL and grid[nextR][nextC] == grid[currR][currC] + 1:
                    return validMove(nextR, nextC)
            return False

        return validMove(0, 0) if grid[0][0] == 0 else False


grid = [[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [
    12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]]
print(Solution().checkValidGrid(grid))
grid = [[0, 3, 6], [5, 8, 1], [2, 7, 4]]
print(Solution().checkValidGrid(grid))
grid = [[24, 11, 22, 17, 4],
        [21, 16, 5, 12, 9],
        [6, 23, 10, 3, 18],
        [15, 20, 1, 8, 13],
        [0, 7, 14, 19, 2]]
print(Solution().checkValidGrid(grid))
