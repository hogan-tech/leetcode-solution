# time complexity: O(c*3^l)
# space complexity: O(l)
from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(suffix: str, r: int, c: int):
            if len(suffix) == 0:
                return True
            if not (0 <= r < ROW and 0 <= c < COL) or suffix[0] != board[r][c]:
                return False
            result = False
            originalChar = board[r][c]
            board[r][c] = "#"
            for dr,dc in ([1,0],[0,1],[-1,0],[0,-1]):
                result = backtrack(suffix[1:], r+dr, c+dc)
                if result:
                    break
            board[r][c] = originalChar
            return result
            
        ROW = len(board)
        COL = len(board[0])
        for row in range(ROW):
            for col in range(COL):
                if backtrack(word, row, col):
                    return True
        return False
        


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

print(Solution().exist(board, word))
