# time complexity: O(m*n)
# space complexity: O(m*n)
from functools import lru_cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        @lru_cache(None)
        def dp(r: int, c: int) -> int:
            if r == rows - 1 and c == cols - 1 and obstacleGrid[r][c] == 0:
                return 1
            if r >= rows or c >= cols or obstacleGrid[r][c] == 1:
                return 0
            return dp(r+1, c) + dp(r, c+1)
        return dp(0, 0)


# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         ROW = len(obstacleGrid)
#         COL = len(obstacleGrid[0])
#         dp = [[0] * (ROW) for _ in range(COL)]
#         dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
#         for r in range(1, ROW):
#             if obstacleGrid[r][0] == 0:
#                 dp[r][0] = dp[r-1][0]
#             else:
#                 dp[r][0] = 0
#         for c in range(1, COL):
#             if obstacleGrid[0][c] == 0:
#                 dp[0][c] = dp[0][c-1]
#             else:
#                 dp[0][c] = 0
#         for r in range(1, ROW):
#             for c in range(1, COL):
#                 if obstacleGrid[r][c] == 0:
#                     dp[r][c] = dp[r-1][c] + dp[r][c-1]
#                 else:
#                     dp[r][c] = 0
#         return dp[ROW-1][COL-1]

obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))
