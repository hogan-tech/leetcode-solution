# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        ROW, COL = len(grid), len(grid[0])
        totalSum = sum(sum(row) for row in grid)

        rowPrefixSum = 0
        for r in range(ROW - 1):
            rowPrefixSum += sum(grid[r])
            if rowPrefixSum * 2 == totalSum:
                return True

        colSumList = [0] * COL
        for row in grid:
            for c in range(COL):
                colSumList[c] += row[c]

        colPrefixSum = 0
        for c in range(COL - 1):
            colPrefixSum += colSumList[c]
            if colPrefixSum * 2 == totalSum:
                return True

        return False


grid = [[1, 4], [2, 3]]
print(Solution().canPartitionGrid(grid))
grid = [[1, 3], [2, 4]]
print(Solution().canPartitionGrid(grid))
