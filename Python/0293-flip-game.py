# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        nextPossibleStates = []

        for index in range(len(currentState) - 1):
            if currentState[index] == '+' and currentState[index + 1] == '+':
                nextState = currentState[:index] + \
                    "--" + currentState[index + 2:]
                nextPossibleStates.append(nextState)

        return nextPossibleStates
