# time complexity: O(m*n)
# space complexity: O(m*n)
from functools import lru_cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])

        @lru_cache(None)
        def dp(r: int, c: int) -> int:
            if r == ROW - 1 and c == COL - 1 and obstacleGrid[r][c] == 0:
                return 1
            if r >= ROW or c >= COL or obstacleGrid[r][c] == 1:
                return 0
            return dp(r+1, c) + dp(r, c+1)
        return dp(0, 0)

# time complexity: O(m*n)
# space complexity: O(m*n)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])
        dp = [[0 for _ in range(COL)] for _ in range(ROW)]
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        for r in range(1, ROW):
            dp[r][0] = 0 if obstacleGrid[r][0] else dp[r - 1][0]
        for c in range(1, COL):
            dp[0][c] = 0 if obstacleGrid[0][c] else dp[0][c - 1]
        for r in range(1, ROW):
            for c in range(1, COL):
                dp[r][c] = 0 if obstacleGrid[r][c] else dp[r - 1][c] + dp[r][c - 1]
        return dp[ROW - 1][COL - 1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))
obstacleGrid = [[0, 1], [0, 0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))
