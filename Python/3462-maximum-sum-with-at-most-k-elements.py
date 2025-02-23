# time complexity: O(nlogn)
# space complexity: O(n*m)
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        nums = []
        ROW = len(grid)
        COL = len(grid[0])
        for r in range(ROW):
            nums.extend(sorted(grid[r])[COL - limits[r]:])
        nums.sort()

        return sum(nums[len(nums) - k:])


grid = [[1, 2], [3, 4]]
limits = [1, 2]
k = 2
print(Solution().maxSum(grid, limits, k))
grid = [[5, 3, 7], [8, 2, 6]]
limits = [2, 2]
k = 3
print(Solution().maxSum(grid, limits, k))
