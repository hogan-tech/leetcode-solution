# time complexity: O(8^(m*n))
# space complexity: O(m*n)

class Solution:
    def tourOfKnight(self, m, n, r, c):
        directions = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]

        def isValidMove(toRow, toCol):
            return (
                0 <= toRow < m
                and 0 <= toCol < n
                and chessboard[toRow][toCol] == 0
            )

        def solveKnightsTour(currR, currC, moveCount):
            if moveCount == m * n:
                return True
            for dirR, dirC in directions:
                nextR = currR + dirR
                nextC = currC + dirC

                if isValidMove(nextR, nextC):
                    chessboard[nextR][nextC] = moveCount
                    if solveKnightsTour(nextR, nextC, moveCount + 1):
                        return True
                    chessboard[nextR][nextC] = 0

            return False

        chessboard = [[0] * n for _ in range(m)]
        chessboard[r][c] = -1
        solveKnightsTour(r, c, 1)
        chessboard[r][c] = 0
        return chessboard


m = 1
n = 1
r = 0
c = 0
print(Solution().tourOfKnight(m, n, r, c))
