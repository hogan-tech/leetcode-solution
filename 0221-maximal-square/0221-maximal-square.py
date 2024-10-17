# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         rows = len(matrix)
#         cols = len(matrix[0]) if rows else 0
#         dpGrid = [[0] * (cols + 1) for _ in range(rows + 1)]
#         maxLen = 0
#         for i in range(1, rows+1):
#             for j in range(1, cols+1):
#                 if matrix[i - 1][j - 1] == "1":
#                     dpGrid[i][j] = min(
#                         dpGrid[i-1][j-1], dpGrid[i][j-1], dpGrid[i-1][j]) + 1
#                     maxLen = max(maxLen, dpGrid[i][j])
#         return maxLen**2

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        dp = [[0] * (COL) for _ in range(ROW)]
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = 0
        print(dp)
        return max([max(row) for row in dp], default=0) ** 2


matrix = [["0", "1"], ["1", "0"]]
print(Solution().maximalSquare(matrix))
