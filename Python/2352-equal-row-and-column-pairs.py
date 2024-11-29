# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import Counter, List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        rowCount = Counter(tuple(row) for row in grid)
        for c in range(len(grid)):
            col = [grid[i][c] for i in range(len(grid))]
            count += rowCount[tuple(col)]
        return count


grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
print(Solution().equalPairs(grid))
