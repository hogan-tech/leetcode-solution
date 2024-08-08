# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dirMap = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        traverse = []
        direction = 0
        step = 1
        while len(traverse) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    if (rStart < rows and cStart < cols and rStart >= 0 and cStart >= 0):
                        traverse.append([rStart, cStart])
                    rStart += dirMap[direction][0]
                    cStart += dirMap[direction][1]
                direction = (direction + 1) % 4
            step += 1
        return traverse


rows = 5
cols = 6
rStart = 1
cStart = 4
print(Solution().spiralMatrixIII(rows, cols, rStart, cStart))
