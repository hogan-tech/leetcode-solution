from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkCols(board: List[List[str]], row: int) -> bool:
            boardSet = set()
            for i in range(9):
                if board[row][i] != '.':
                    if board[row][i] in boardSet:
                        return False
                    boardSet.add(board[row][i])
            return True

        def checkRows(board: List[List[str]], col: int) -> bool:
            boardSet = set()
            for i in range(9):
                if board[i][col] != '.':
                    if board[i][col] in boardSet:
                        return False
                    boardSet.add(board[i][col])
            return True

        def checkBox(board: List[List[str]], row: int, col: int) -> bool:
            boardSet = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] != '.':
                        if board[i][j] in boardSet:
                            return False
                    boardSet.add(board[i][j])
            return True

        for i in range(9):
            if not checkCols(board, i):
                return False
            if not checkRows(board, i):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checkBox(board, i, j):
                    return False
        return True