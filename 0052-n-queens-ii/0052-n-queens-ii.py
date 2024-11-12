# time complexity: O(n!)
# space complexity: O(n)
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        return len(self.solveNQueens(n))

    def solveNQueens(self, n: int) -> List[List[str]]:
        def createBoard(state: List[str]):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(row: int, diagonals: set, antiDiagonals: set, cols: set, state: List[str]):
            if row == n:
                ans.append(createBoard(state))
                return

            for col in range(n):
                currDiagonal = row - col
                currAntiDiagonal = row + col
                if (
                    col in cols
                    or currDiagonal in diagonals
                    or currAntiDiagonal in antiDiagonals
                ):
                    continue

                cols.add(col)
                diagonals.add(currDiagonal)
                antiDiagonals.add(currAntiDiagonal)
                state[row][col] = "Q"

                backtrack(row + 1, diagonals, antiDiagonals, cols, state)

                cols.remove(col)
                diagonals.remove(currDiagonal)
                antiDiagonals.remove(currAntiDiagonal)
                state[row][col] = "."

        ans = []
        emptyBoard = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), emptyBoard)
        return ans


n = 4
print(Solution().totalNQueens(n))
