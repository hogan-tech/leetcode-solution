# time complexity: O(r*c*k^2)
# space complexity: O(r*c)
from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ROW = len(grid)
        COL = len(grid[0])
        result = [[0] * (COL - k + 1) for _ in range(ROW - k + 1)]

        for r in range(ROW - k + 1):
            for c in range(COL - k + 1):
                blockVals = []
                for blockR in range(r, r + k):
                    for blockC in range(c, c + k):
                        blockVals.append(grid[blockR][blockC])

                if len(blockVals) <= 1:
                    result[r][c] = 0
                    continue

                distinctVals = sorted(set(blockVals))
                if len(distinctVals) == 1:
                    result[r][c] = 0
                    continue

                mindiff = float('inf')
                for t in range(1, len(distinctVals)):
                    diff = distinctVals[t] - distinctVals[t - 1]
                    if diff < mindiff:
                        mindiff = diff
                        if mindiff == 0:
                            break

                result[r][c] = mindiff

        return result


grid = [[1, 8], [3, -2]]
k = 2
print(Solution().minAbsDiff(grid, k))
grid = [[3, -1]]
k = 1
print(Solution().minAbsDiff(grid, k))
grid = [[1, -2, 3], [2, 3, 5]]
k = 2
print(Solution().minAbsDiff(grid, k))
