# time complexity: O(logmn)
# space complexity: O(1)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])
        left = 0
        right = ROW * COL - 1
        if ROW == 0:
            return False
        while left <= right:
            mid = left + (right - left) // 2
            value = matrix[mid//COL][mid % COL]
            if value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
            else:
                return True
        return False
'''

0 1 2 3 4 5 6 7 8

0 1 2
3 4 5
6 7 8

row = idx // COL
col = idx % COL
'''

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(Solution().searchMatrix(matrix, target))
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
print(Solution().searchMatrix(matrix, target))
