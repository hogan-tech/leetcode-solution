# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        dp = [[0 for _ in range(COL)] for _ in range(ROW)]
        maxLen = 0
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == "1":
                    dp[r][c] = min(dp[r-1][c-1], dp[r][c-1], dp[r-1][c]) + 1
                    maxLen = max(maxLen, dp[r][c])
        return maxLen ** 2


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(Solution().maximalSquare(matrix))
matrix = [["0", "1"], ["1", "0"]]
print(Solution().maximalSquare(matrix))
matrix = [["0"]]
print(Solution().maximalSquare(matrix))
