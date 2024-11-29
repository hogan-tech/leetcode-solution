# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1),
                     (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows = len(board)
        cols = len(board[0])
        copyBoard = [[board[row][col]
                      for col in range(cols)] for row in range(rows)]
        for row in range(rows):
            for col in range(cols):
                liveNeighbors = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copyBoard[r][c] == 1):
                        liveNeighbors += 1
                if copyBoard[row][col] == 1 and (liveNeighbors < 2 or liveNeighbors > 3):
                    board[row][col] = 0
                if copyBoard[row][col] == 0 and liveNeighbors == 3:
                    board[row][col] = 1


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(Solution().gameOfLife(board))
