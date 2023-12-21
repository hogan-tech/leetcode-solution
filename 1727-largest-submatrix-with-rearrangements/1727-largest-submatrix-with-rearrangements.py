# time complexity: O(mnlogn)
# space complexity: O(mn)
from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            currRow = sorted(matrix[row], reverse=True)
            for i in range(n):
                ans = max(ans, currRow[i] * (i + 1))

        return ans


matrix = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]
print(Solution().largestSubmatrix(matrix))
