from typing import List


class Solution:
    def backtrack(self, row: int, col: int, suffix: str):
        if len(suffix) == 0:
            return True
        if not (0 <= row < self.rows and 0 <= col < self.cols) or self.board[row][col] != suffix[0]:
            return False
        result = False
        originalChar = self.board[row][col]
        self.board[row][col] = '#'
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            result = self.backtrack(row+rowOffset, col+colOffset, suffix[1:])
            if result:
                break
        self.board[row][col] = originalChar
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        for row in range(self.rows):
            for col in range(self.cols):
                if self.backtrack(row, col, word):
                    return True
        return False