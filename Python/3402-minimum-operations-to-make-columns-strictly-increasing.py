# time complexity: O(mn)
# space complexity: O(1)
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        count = 0
        for col in range(len(grid[0])):
            curr = grid[0][col]
            for row in range(1, len(grid)):
                if grid[row][col] <= curr:
                    count += curr - grid[row][col] + 1
                    curr += 1
                else:
                    curr = grid[row][col]
        return count


grid = [[3, 2], [1, 3], [3, 4], [0, 1]]
print(Solution().minimumOperations(grid))
grid = [[3, 2, 1], [2, 1, 0], [1, 2, 3]]
print(Solution().minimumOperations(grid))
