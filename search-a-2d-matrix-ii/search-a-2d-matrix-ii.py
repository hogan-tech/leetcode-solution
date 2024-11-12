# time complexity: O(logn!)
# space complexity: O(1)
from typing import List


class Solution:
    def binarySearch(self, matrix, target, start, vertical):
        left = start
        right = len(matrix[0]) - 1 if vertical else len(matrix) - 1
        while left <= right:
            mid = (right + left) // 2
            if vertical:
                if matrix[start][mid] < target:
                    left = mid + 1
                elif matrix[start][mid] > target:
                    right = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    left = mid + 1
                elif matrix[mid][start] > target:
                    right = mid - 1
                else:
                    return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None:
            return False
        for i in range(min(len(matrix), len(matrix[0]))):
            verticalFound = self.binarySearch(matrix, target, i, True)
            horizontalFound = self.binarySearch(matrix, target, i, False)
            if verticalFound or horizontalFound:
                return True
        return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
    3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]

target = 20

print(Solution().searchMatrix(matrix, target))
