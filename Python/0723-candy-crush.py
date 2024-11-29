from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])

        def find():
            crushedSet = set()
            for r in range(1, m-1):
                for c in range(n):
                    if board[r][c] == 0:
                        continue
                    if board[r][c] == board[r-1][c] == board[r+1][c]:
                        crushedSet.add((r, c))
                        crushedSet.add((r-1, c))
                        crushedSet.add((r+1, c))
            for r in range(m):
                for c in range(1, n-1):
                    if board[r][c] == 0:
                        continue
                    if board[r][c] == board[r][c-1] == board[r][c+1]:
                        crushedSet.add((r, c))
                        crushedSet.add((r, c-1))
                        crushedSet.add((r, c+1))
            return crushedSet

        def crush(crushedSet):
            for (r, c) in crushedSet:
                board[r][c] = 0

        def drop():
            for c in range(n):
                lowestZero = -1
                for r in range(m-1, -1, -1):
                    if board[r][c] == 0:
                        lowestZero = max(lowestZero, r)
                    elif lowestZero >= 0:
                        board[r][c], board[lowestZero][c] = board[lowestZero][c], board[r][c]
                        lowestZero -= 1

        crushedSet = find()
        while crushedSet:
            crush(crushedSet)
            drop()
            crushedSet = find()
        return board


board = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414], [
    5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2], [4, 1, 4, 4, 1014]]


print(Solution().candyCrush(board))
