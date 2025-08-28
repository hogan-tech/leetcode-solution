# time complexity: O(m*n)
# space complexity: O(m*n)
from functools import cache
from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(cx, cy, direction, turn, target):
            nx, ny = cx + DIRS[direction][0], cy + DIRS[direction][1]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != target:
                return 0
            maxStep = dfs(nx, ny, direction, turn, 2 - target)
            if turn:
                maxStep = max(
                    maxStep,
                    dfs(nx, ny, (direction + 1) % 4, False, 2 - target),
                )
            return maxStep + 1

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for direction in range(4):
                        result = max(result, dfs(i, j, direction, True, 2) + 1)
        return result


grid = [[2, 2, 1, 2, 2], [2, 0, 2, 2, 0], [
    2, 0, 1, 1, 0], [1, 0, 2, 2, 2], [2, 0, 0, 2, 2]]
print(Solution().lenOfVDiagonal(grid))
grid = [[2, 2, 2, 2, 2], [2, 0, 2, 2, 0], [
    2, 0, 1, 1, 0], [1, 0, 2, 2, 2], [2, 0, 0, 2, 2]]
print(Solution().lenOfVDiagonal(grid))
grid = [[1, 2, 2, 2, 2], [2, 2, 2, 2, 0], [
    2, 0, 0, 0, 0], [0, 0, 2, 2, 2], [2, 0, 0, 2, 0]]
print(Solution().lenOfVDiagonal(grid))
grid = [[1]]
print(Solution().lenOfVDiagonal(grid))
