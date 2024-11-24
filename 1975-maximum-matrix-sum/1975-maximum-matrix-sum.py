# time complexity: O(n*m)
# space complexity: O(1)
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalSum = 0
        minAbsVal = float("inf")
        negativeCount = 0

        for row in matrix:
            for val in row:
                totalSum += abs(val)
                if val < 0:
                    negativeCount += 1
                minAbsVal = min(minAbsVal, abs(val))

        if negativeCount % 2 != 0:
            totalSum -= 2 * minAbsVal

        return totalSum


matrix = [[1, -1], [-1, 1]]
print(Solution().maxMatrixSum(matrix))
matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
print(Solution().maxMatrixSum(matrix))
