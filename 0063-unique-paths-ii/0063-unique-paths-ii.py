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