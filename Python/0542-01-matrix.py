# time complexity: O(m*n)
# space complexity: O(m*n)
from asyncio import Queue
from collections import deque
from typing import List


# BFS
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ROW = len(matrix)
        COL = len(matrix[0])
        queue = deque()
        dist = [[float('inf') for _ in range(COL)] for _ in range(ROW)]
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))
        while queue:
            currR, currC = queue.popleft()
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL:
                    if dist[nextR][nextC] > dist[currR][currC] + 1:
                        dist[nextR][nextC] = dist[currR][currC] + 1
                        queue.append((nextR, nextC))
        return dist

# time complexity: O(m*n)
# space complexity: O(1)
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ROW = len(matrix)
        COL = len(matrix[0])
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] > 0:
                    above = matrix[r-1][c] if r > 0 else float('inf')
                    left = matrix[r][c-1] if c > 0 else float('inf')
                    matrix[r][c] = min(above, left) + 1

        for r in range(ROW - 1, -1, -1):
            for c in range(COL - 1, -1, -1):
                if matrix[r][c] > 0:
                    below = matrix[r+1][c] if r < ROW - 1 else float('inf')
                    right = matrix[r][c+1] if c < COL - 1 else float('inf')
                    minDistance = min(below, right) + 1
                    matrix[r][c] = min(matrix[r][c], minDistance)
        return matrix

# time complexity: O(m*n)
# space complexity: O(m*n)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = [row[:] for row in mat]
        m, n = len(dp), len(dp[0])

        for row in range(m):
            for col in range(n):
                minNeighbor = float('inf')
                if dp[row][col] != 0:
                    if row > 0:
                        minNeighbor = min(minNeighbor, dp[row - 1][col])
                    if col > 0:
                        minNeighbor = min(minNeighbor, dp[row][col - 1])

                    dp[row][col] = minNeighbor + 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                minNeighbor = float('inf')
                if dp[row][col] != 0:
                    if row < m - 1:
                        minNeighbor = min(minNeighbor, dp[row + 1][col])
                    if col < n - 1:
                        minNeighbor = min(minNeighbor, dp[row][col + 1])

                    dp[row][col] = min(dp[row][col], minNeighbor + 1)

        return dp


mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(Solution().updateMatrix(mat))
mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(Solution().updateMatrix(mat))
mat = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [
    0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
print(Solution().updateMatrix(mat))
