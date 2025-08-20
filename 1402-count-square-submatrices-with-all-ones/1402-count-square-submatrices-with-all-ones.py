# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        dp = [[0] * (COL + 1) for _ in range(ROW + 1)]

        result = 0
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    result += dp[i][j]
        return result


matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]

print(Solution().countSquares(matrix))
