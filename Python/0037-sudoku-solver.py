# time complexity: O(9!^9)
# space complexity: O(1)
from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board)

        rows, cols, boxes = defaultdict(
            set), defaultdict(set), defaultdict(set)

        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue

                digit = int(board[r][c])
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[(r // 3) * 3 + c // 3].add(digit)

        def isValid(r: int, c: int, digit: int):
            boxId = (r // 3) * 3 + c // 3
            return digit not in rows[r] and digit not in cols[c] and digit not in boxes[boxId]

        def backtrack(r: int, c: int):
            if r == n - 1 and c == n:
                return True
            elif c == n:
                c = 0
                r += 1

            if board[r][c] != '.':
                return backtrack(r, c + 1)

            boxId = (r // 3) * 3 + c // 3
            for digit in range(1, n + 1):
                if not isValid(r, c, digit):
                    continue

                board[r][c] = str(digit)
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[boxId].add(digit)

                if backtrack(r, c + 1):
                    return True

                board[r][c] = '.'
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[boxId].remove(digit)

            return False

        backtrack(0, 0)


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
