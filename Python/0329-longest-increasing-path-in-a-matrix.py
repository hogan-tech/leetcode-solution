# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        visited = [[0 for _ in range(COL)] for _ in range(ROW)]
        maxPath = 0

        def dfs(currR: int, currC: int) -> int:
            if visited[currR][currC] != 0:
                return visited[currR][currC]
            for dirR, dirC in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nextR = currR + dirR
                nextC = currC + dirC
                if 0 <= nextR < ROW and 0 <= nextC < COL and matrix[nextR][nextC] > matrix[currR][currC]:
                    visited[currR][currC] = max(
                        visited[currR][currC], dfs(nextR, nextC))
            visited[currR][currC] += 1
            return visited[currR][currC]

        for r in range(ROW):
            for c in range(COL):
                maxPath = max(maxPath, dfs(r, c))
        return maxPath


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(Solution().longestIncreasingPath(matrix))
matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
print(Solution().longestIncreasingPath(matrix))
matrix = [[1]]
print(Solution().longestIncreasingPath(matrix))
