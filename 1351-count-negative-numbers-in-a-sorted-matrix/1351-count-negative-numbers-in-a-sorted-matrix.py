# time complexity: O(mlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid)):
            left = 0
            right = len(grid[0]) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if grid[row][mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += (len(grid[0]) - left)
        return count


grid = [[3, 2], [1, 0]]
print(Solution().countNegatives(grid))
