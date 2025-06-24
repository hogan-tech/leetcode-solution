# time complexity: O(m*n)
# space complexity: O(1)
from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(x: int, y: int):
            board[x][y] = "#"
            for X, Y in ((x + 1, y), (x, y + 1), (x-1, y), (x, y-1)):
                if 0 <= X < m and 0 <= Y < n and board[X][Y] == 'O':
                    dfs(X, Y)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)

        for i in range(n):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[m-1][i] == 'O':
                dfs(m-1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

        return board


# time complexity: O(m*n)
# space complexity: O(1)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(x: int, y: int):
            board[x][y] = "#"
            for X, Y in ((x + 1, y), (x, y + 1), (x-1, y), (x, y-1)):
                if 0 <= X < m and 0 <= Y < n and board[X][Y] == 'O':
                    dfs(X, Y)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)

        for i in range(n):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[m-1][i] == 'O':
                dfs(m-1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

        return board


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            board[r][c] = "#"

            while queue:
                currR, currC = queue.popleft()

                for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nextR = currR + dR
                    nextC = currC + dC
                    if 0 <= nextR < ROW and 0 <= nextC < COL and board[nextR][nextC] == 'O':
                        board[nextR][nextC] = '#'
                        queue.append((nextR, nextC))

        for r in range(ROW):
            if board[r][0] == 'O':
                bfs(r, 0)
            if board[r][COL - 1] == 'O':
                bfs(r, COL - 1)

        for c in range(COL):
            if board[0][c] == 'O':
                bfs(0, c)
            if board[ROW - 1][c] == 'O':
                bfs(ROW - 1, c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'

        return board


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
         ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
print(Solution().solve(board))
board = [["X"]]
print(Solution().solve(board))
board = [["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"], ["X", "O", "O", "X", "O", "X", "O", "O", "O", "O", "X", "O", "O", "X", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X", "O"], ["O", "X", "X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "X", "O"], ["O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O"], ["O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"], [
    "O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"], ["X", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X"], ["O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "X", "O", "O"], ["O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "X", "O", "O", "X"], ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]]
print(Solution().solve(board))
