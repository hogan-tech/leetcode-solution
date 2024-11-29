# time complexity: O(m*n)
# space complexity: O(1)
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


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
         ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

print(Solution().solve(board))
