# time complexity: O(n!)
# space complexity: O(n^2)
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [['.'] * n for _ in range(n)]
        colSet = set()
        posDiagonal = set()
        negDiagonal = set()
        def backtrack(r: int):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
            for c in range(n):
                if c in colSet or (r + c) in posDiagonal or (r - c) in negDiagonal:
                    continue
                colSet.add(c)
                posDiagonal.add(r + c)
                negDiagonal.add(r - c)
                board[r][c] = 'Q'
                backtrack(r+1)

                colSet.remove(c)
                posDiagonal.remove(r + c)
                negDiagonal.remove(r - c)
                board[r][c] = '.'

        backtrack(0)
        return result


n = 4
print(Solution().solveNQueens(n))
