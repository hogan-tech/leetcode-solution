# time complexity: O(n!)
# space complexity: O(n)
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        result = []
        emptyBoard = [["."] * n for _ in range(n)]

        def backtrack(r: int, diagonals: set, antiDiagonals: set, cols: set, state: List[str]):
            if r == n:
                board = []
                for row in state:
                    board.append("".join(row))
                result.append(board)
                return

            for c in range(n):
                currDiagonal = r - c
                currAntiDiagonal = r + c
                if (
                    c in cols
                    or currDiagonal in diagonals
                    or currAntiDiagonal in antiDiagonals
                ):
                    continue
                cols.add(c)
                diagonals.add(currDiagonal)
                antiDiagonals.add(currAntiDiagonal)
                state[r][c] = "Q"

                backtrack(r + 1, diagonals, antiDiagonals, cols, state)

                cols.remove(c)
                diagonals.remove(currDiagonal)
                antiDiagonals.remove(currAntiDiagonal)
                state[r][c] = "."

        backtrack(0, set(), set(), set(), emptyBoard)
        return len(result)


n = 4
print(Solution().totalNQueens(n))
n = 1
print(Solution().totalNQueens(n))
