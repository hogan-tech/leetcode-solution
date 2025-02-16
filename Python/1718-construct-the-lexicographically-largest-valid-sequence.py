# time complexity: O(n!)
# space complexity: O(n)
from typing import List


class Solution:
    def constructDistancedSequence(self, target: int) -> List[int]:
        resultSequence = [0] * (target * 2 - 1)

        isNumberUsed = [False] * (target + 1)

        self.findLexicographicallyLargestSequence(
            0, resultSequence, isNumberUsed, target)

        return resultSequence

    def findLexicographicallyLargestSequence(self, currIdx, resultSequence, isNumberUsed, target):
        if currIdx == len(resultSequence):
            return True

        if resultSequence[currIdx] != 0:
            return self.findLexicographicallyLargestSequence(
                currIdx + 1,
                resultSequence,
                isNumberUsed,
                target,
            )

        for numberToPlace in range(target, 0, -1):
            if isNumberUsed[numberToPlace]:
                continue

            isNumberUsed[numberToPlace] = True
            resultSequence[currIdx] = numberToPlace

            if numberToPlace == 1:
                if self.findLexicographicallyLargestSequence(
                    currIdx + 1,
                    resultSequence,
                    isNumberUsed,
                    target,
                ):
                    return True
            elif (
                currIdx + numberToPlace < len(resultSequence)
                and resultSequence[currIdx + numberToPlace] == 0
            ):
                resultSequence[currIdx + numberToPlace] = (
                    numberToPlace
                )

                if self.findLexicographicallyLargestSequence(
                    currIdx + 1,
                    resultSequence,
                    isNumberUsed,
                    target,
                ):
                    return True

                resultSequence[currIdx + numberToPlace] = 0

            resultSequence[currIdx] = 0
            isNumberUsed[numberToPlace] = False

        return False


n = 3
print(Solution().constructDistancedSequence(n))
n = 5
print(Solution().constructDistancedSequence(n))
