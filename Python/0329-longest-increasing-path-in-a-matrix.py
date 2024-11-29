# time complexity: O(m*n)
# space complexity: O(m*n)
from collections import defaultdict
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        cache = [[0 for i in range(COL)] for j in range(ROW)]
        maxPath = 0
        for i in range(ROW):
            for j in range(COL):
                maxPath = max(maxPath, self.dfs(matrix, i, j, cache))

        return maxPath

    def dfs(self, matrix: List[List[int]], currR: int, currC: int, cache: defaultdict) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        if cache[currR][currC] != 0:
            return cache[currR][currC]
        for dirR, dirC in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nextR = currR + dirR
            nextC = currC + dirC
            if 0 <= nextR < ROW and 0 <= nextC < COL and matrix[nextR][nextC] > matrix[currR][currC]:
                cache[currR][currC] = max(
                    cache[currR][currC], self.dfs(matrix, nextR, nextC, cache))
        cache[currR][currC] += 1
        return cache[currR][currC]


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(Solution().longestIncreasingPath(matrix))
