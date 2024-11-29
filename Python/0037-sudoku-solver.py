# time complexity: O(9!^9)
# space complexity: O(1)
from collections import defaultdict


class Solution:
    def solveSudoku(self, board):

        def couldPlace(d, row, col):
            return not (
                d in rows[row]
                or d in columns[col]
                or d in boxes[boxIndex(row, col)]
            )

        def placeNumber(d, row, col):
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[boxIndex(row, col)][d] += 1
            board[row][col] = str(d)

        def removeNumber(d, row, col):
            rows[row][d] -= 1
            columns[col][d] -= 1
            boxes[boxIndex(row, col)][d] -= 1
            if rows[row][d] == 0:
                del rows[row][d]
            if columns[col][d] == 0:
                del columns[col][d]
            if boxes[boxIndex(row, col)][d] == 0:
                del boxes[boxIndex(row, col)][d]
            board[row][col] = "."

        def placeNextNumbers(row, col):
            if col == N - 1 and row == N - 1:
                sudokuSolved[0] = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            if board[row][col] == ".":
                for d in range(1, 10):
                    if couldPlace(d, row, col):
                        placeNumber(d, row, col)
                        placeNextNumbers(row, col)
                        if sudokuSolved[0]:
                            return
                        removeNumber(d, row, col)
            else:
                placeNextNumbers(row, col)

        n = 3
        N = n * n

        def boxIndex(row, col): return (row // n) * n + col // n

        rows = [defaultdict(int) for _ in range(N)]
        columns = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    d = int(board[i][j])
                    placeNumber(d, i, j)

        sudokuSolved = [False]
        backtrack()


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(Solution().solveSudoku(board))
