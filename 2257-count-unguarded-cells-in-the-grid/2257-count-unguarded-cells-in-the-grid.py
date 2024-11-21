from collections import deque
from typing import List


class Solution:
    Guarded = 0
    Unguarded = 1
    Guard = 2
    Wall = 3
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ROW = m
        COL = n
        board = [[self.Unguarded] * COL for _ in range(ROW)]
        queue = deque()
        for i, j in guards:
            board[i][j] = self.Guard
            queue.append((i,j))
        for i, j in walls:
            board[i][j] = self.Wall
        while queue:
            currR, currC = queue.popleft()

            for r in range(currR - 1, -1, -1):
                if board[r][currC] == self.Wall or board[r][currC] == self.Guard:
                    break
                board[r][currC] = self.Guarded

            for r in range(currR + 1, ROW):
                if board[r][currC] == self.Wall or board[r][currC] == self.Guard:
                    break
                board[r][currC] = self.Guarded

            for c in range(currC - 1, -1, -1):
                if board[currR][c] == self.Wall or board[currR][c] == self.Guard:
                    break
                board[currR][c] = self.Guarded

            for c in range(currC + 1, COL):
                if board[currR][c] == self.Wall or board[currR][c] == self.Guard:
                    break
                board[currR][c] = self.Guarded
        
        return sum([board[i].count(1) for i in range(ROW)])


m = 4
n = 6
guards = [[0, 0], [1, 1], [2, 3]]
walls = [[0, 1], [2, 2], [1, 4]]
print(Solution().countUnguarded(m, n, guards, walls))

m = 3
n = 3
guards = [[1, 1]]
walls = [[0, 1], [1, 0], [2, 1], [1, 2]]
print(Solution().countUnguarded(m, n, guards, walls))
