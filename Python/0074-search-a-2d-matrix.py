from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        if rows == 0:
            return False
        while left <= right:
            mid = left + (right - left) // 2
            value = matrix[mid//cols][mid % cols]
            if value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
            else:
                return True
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(Solution().searchMatrix(matrix, target))
