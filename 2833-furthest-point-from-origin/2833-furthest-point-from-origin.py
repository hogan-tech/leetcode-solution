class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        movesLeft = moves.replace('_', 'L')
        movesRight = moves.replace('_', 'R')
        ansLeft = -movesLeft.count('L') + movesLeft.count('R')
        ansRight = movesRight.count('R') - movesRight.count('L')

        return max(abs(ansLeft), abs(ansRight))


moves = "_R"

print(Solution().furthestDistanceFromOrigin(moves))
