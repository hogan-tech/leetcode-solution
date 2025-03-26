# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        remainder = grid[0][0] % x
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                currRemainder = grid[r][c] % x
                if remainder != currRemainder:
                    return -1
                else:
                    nums.append(grid[r][c])
        nums.sort()
        midLeft = (len(nums) - 1) // 2
        midRight = midLeft + 1
        resultMidLeft = 0
        resultMidRight = 0
        for num in nums:
            if midLeft < len(nums):
                resultMidLeft += (abs(nums[midLeft] - num) // x)
            if midRight < len(nums):
                resultMidRight += (abs(nums[midRight] - num) // x)
        return min(resultMidLeft, resultMidRight)


grid = [[4], [5]]
x = 1
print(Solution().minOperations(grid, x))
grid = [[2, 4], [6, 8]]
x = 2
print(Solution().minOperations(grid, x))
grid = [[1, 5], [2, 3]]
x = 1
print(Solution().minOperations(grid, x))
grid = [[1, 2], [3, 4]]
x = 2
print(Solution().minOperations(grid, x))
