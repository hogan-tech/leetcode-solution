# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ROW = 8
        COL = 8
        attacks = []
        directions = [[1, -1], [1, 0], [1, 1],
                      [0, -1], [0, 1],
                      [-1, -1], [-1, 0], [-1, 1]]
        kingR = king[0]
        kingC = king[1]

        for dR, dC in directions:
            nextR = kingR + dR
            nextC = kingC + dC
            while 0 <= nextR < ROW and 0 <= nextC < COL:
                if [nextR, nextC] in queens:
                    attacks.append([nextR, nextC])
                    break
                nextR += dR
                nextC += dC

        return attacks


queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
king = [0, 0]
print(Solution().queensAttacktheKing(queens, king))
queens = [[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]]
king = [3, 3]
print(Solution().queensAttacktheKing(queens, king))
