# time complexity: O(n^2) -> O(1)
# space complexity: O(n^2) -> O(1)
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                value = board[r][c]
                if value == '.':
                    continue

                if value in rows[r]:
                    return False
                rows[r].add(value)

                if value in cols[c]:
                    return False
                cols[c].add(value)

                idx = (r // 3) * 3 + c // 3
                if value in boxes[idx]:
                    return False
                boxes[idx].add(value)

        return True


'''

0 0 0 1 1 1 2 2 2 <- c // 3
0 1 2 3 4 5 6 7 8 <-    c


00 01 02 03 04 05 06 07 08
10 11 12 13 14 15 16 17 18
20 21 22 23 24 25 26 27 28


'''


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().isValidSudoku(board))

board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]
print(Solution().isValidSudoku(board))
