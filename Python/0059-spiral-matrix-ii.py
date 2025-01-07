# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0 for _ in range(n)] for _ in range(n)]
        ROW = n
        COL = n
        direction = 1
        row = 0
        col = -1
        i = 1
        while ROW > 0 and COL > 0:
            for _ in range(COL):
                col += direction
                grid[row][col] = i
                i += 1
            ROW -= 1
            for _ in range(ROW):
                row += direction
                grid[row][col] = i
                i += 1
            COL -= 1
            direction *= -1

        return grid


n = 3
print(Solution().generateMatrix(3))
n = 1
print(Solution().generateMatrix(1))
