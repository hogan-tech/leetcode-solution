# time complexity: O(1)
# space complexity: O(1)
from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        OCount = 0
        XCount = 0
        OWin = False
        XWin = False

        def checkWin(player: str):
            for r in range(3):
                if board[r][0] == board[r][1] == board[r][2] == player:
                    return True
            for c in range(3):
                if board[0][c] == board[1][c] == board[2][c] == player:
                    return True
            if board[0][0] == board[1][1] == board[2][2] == player:
                return True
            if board[2][0] == board[1][1] == board[0][2] == player:
                return True
            return False

        for r in range(3):
            for c in range(3):
                if board[r][c] == 'X':
                    XCount += 1
                if board[r][c] == 'O':
                    OCount += 1

        if OCount > XCount:
            return False
        if XCount > OCount + 1:
            return False

        OWin = checkWin('O')
        XWin = checkWin('X')
        if OWin and XWin:
            return False
        if XWin and XCount == OCount:
            return False
        if OWin and XCount > OCount:
            return False
        return True


board = ["XXX",
         "OOX",
         "OOX"]
print(Solution().validTicTacToe(board))
board = ["OXX",
         "XOX",
         "OXO"]
print(Solution().validTicTacToe(board))
board = ["XXX", "   ", "OOO"]
print(Solution().validTicTacToe(board))
board = ["O  ", "   ", "   "]
print(Solution().validTicTacToe(board))
board = ["XOX", " X ", "   "]
print(Solution().validTicTacToe(board))
board = ["XOX", "O O", "XOX"]
print(Solution().validTicTacToe(board))
