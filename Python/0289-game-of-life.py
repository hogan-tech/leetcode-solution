# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        ROW = len(board)
        COL = len(board[0])
        copyBoard = [[board[r][c]for c in range(COL)] for r in range(ROW)]
        for r in range(ROW):
            for c in range(COL):
                liveNeighbors = 0
                for dR, dC in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
                    nextR = r + dR
                    nextC = c + dC
                    if 0 <= nextR < ROW and 0 <= nextC < COL and copyBoard[nextR][nextC] == 1:
                        liveNeighbors += 1
                if copyBoard[r][c] == 1 and (liveNeighbors < 2 or liveNeighbors > 3):
                    board[r][c] = 0
                if copyBoard[r][c] == 0 and liveNeighbors == 3:
                    board[r][c] = 1


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(Solution().gameOfLife(board))
board = [[1, 1], [1, 0]]
print(Solution().gameOfLife(board))
