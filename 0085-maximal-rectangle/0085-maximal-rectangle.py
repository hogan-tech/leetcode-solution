# time complexity: O(n^2 * m)
# space complexity: O(nm)
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxArea = max(maxArea, width * (i-k+1))
        return maxArea


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(Solution().maximalRectangle(matrix))
