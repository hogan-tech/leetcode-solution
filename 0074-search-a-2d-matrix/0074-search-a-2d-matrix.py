from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == 0:
            return False
        left = 0
        right = rows*cols - 1
        while left <= right:
            mid = left + (right - left) // 2
            element = matrix[mid // cols][mid % cols]
            if element == target:
                return True
            if target < element:
                right = mid - 1
            else:
                left = mid + 1
        return False