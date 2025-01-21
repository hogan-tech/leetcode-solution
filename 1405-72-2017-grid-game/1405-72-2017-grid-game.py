# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        firstRowSum = sum(grid[0])
        secondRowSum = 0
        minimumSum = float("inf")
        for turnIndex in range(len(grid[0])):
            firstRowSum -= grid[0][turnIndex]
            minimumSum = min(minimumSum, max(firstRowSum, secondRowSum))
            secondRowSum += grid[1][turnIndex]
        return minimumSum


grid = [[2, 5, 4], [1, 5, 1]]
print(Solution().gridGame(grid))
grid = [[3, 3, 1], [8, 5, 2]]
print(Solution().gridGame(grid))
grid = [[1, 3, 1, 15], [1, 3, 3, 1]]
print(Solution().gridGame(grid))
