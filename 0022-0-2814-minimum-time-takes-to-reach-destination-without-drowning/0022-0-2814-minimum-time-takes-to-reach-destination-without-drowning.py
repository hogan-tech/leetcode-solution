# time complexity: O(m*n)
# space complecity: O(m*n)
from collections import deque
from typing import List


class Solution:
    def minimumSeconds(self, land: List[List[str]]) -> int:
        ROW = len(land)
        COL = len(land[0])
        flood = deque()
        moves = deque()
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seconds = 0

        for r in range(ROW):
            for c in range(COL):
                if land[r][c] == 'S':
                    moves.append((r, c))
                if land[r][c] == '*':
                    flood.append((r, c))

        while moves:
            spread = len(flood)
            for _ in range(spread):
                floodR, floodC = flood.popleft()
                for dR, dC in DIRS:
                    nextR = floodR + dR
                    nextC = floodC + dC
                    if 0 <= nextR < ROW and 0 <= nextC < COL and land[nextR][nextC] == '.':
                        land[nextR][nextC] = '*'
                        flood.append((nextR, nextC))

            move = len(moves)
            for _ in range(move):
                moveR, moveC = moves.popleft()
                if land[moveR][moveC] == 'D':
                    return seconds
                for dR, dC in DIRS:
                    nextR = moveR + dR
                    nextC = moveC + dC
                    if 0 <= nextR < ROW and 0 <= nextC < COL:
                        if land[nextR][nextC] == '.' or land[nextR][nextC] == 'D':
                            if land[nextR][nextC] != 'D':
                                land[nextR][nextC] = '*'
                            moves.append((nextR, nextC))

            seconds += 1
        return -1


land = [["D", ".", "*"], [".", ".", "."], [".", "S", "."]]
print(Solution().minimumSeconds(land))
land = [["D", "X", "*"], [".", ".", "."], [".", ".", "S"]]
print(Solution().minimumSeconds(land))
land = [["D", ".", ".", ".", "*", "."], [".", "X", ".",
                                         "X", ".", "."], [".", ".", ".", ".", "S", "."]]
print(Solution().minimumSeconds(land))
