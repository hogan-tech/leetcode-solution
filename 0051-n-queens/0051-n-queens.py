# time complexity: O(n!)
# space complexity: O(n^2)
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Making use of a helper function to get the
        # solutions in the correct output format
        def createBoard(state: List[str]):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(row: int, diagonals: set, antiDiagonals: set, cols: set, state: List[str]):
            # Base case - N queens have been placed
            if row == n:
                ans.append(createBoard(state))
                return

            for col in range(n):
                currDiagonal = row - col
                currAntiDiagonal = row + col
                # If the queen is not placeable
                if (
                    col in cols
                    or currDiagonal in diagonals
                    or currAntiDiagonal in antiDiagonals
                ):
                    continue

                # "Add" the queen to the board
                cols.add(col)
                diagonals.add(currDiagonal)
                antiDiagonals.add(currAntiDiagonal)
                state[row][col] = "Q"

                # Move on to the next row with the updated board state
                backtrack(row + 1, diagonals, antiDiagonals, cols, state)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(currDiagonal)
                antiDiagonals.remove(currAntiDiagonal)
                state[row][col] = "."

        ans = []
        emptyBoard = [["."] * n for _ in range(n)]
        print(emptyBoard)
        backtrack(0, set(), set(), set(), emptyBoard)
        return ans


n = 4
print(Solution().solveNQueens(n))
