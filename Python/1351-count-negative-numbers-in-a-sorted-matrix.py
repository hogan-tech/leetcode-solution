# time complexity: O(mlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += (len(row) - left)
        return count


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(Solution().countNegatives(grid))
grid = [[3, 2], [1, 0]]
print(Solution().countNegatives(grid))
