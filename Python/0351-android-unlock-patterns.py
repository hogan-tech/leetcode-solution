# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def __init__(self):
        self.cantSkip = [[0 for __ in range(10)] for _ in range(10)]
        self.cantSkip[1][3] = self.cantSkip[3][1] = 2
        self.cantSkip[1][7] = self.cantSkip[7][1] = 4
        self.cantSkip[3][9] = self.cantSkip[9][3] = 6
        self.cantSkip[7][9] = self.cantSkip[9][7] = 8
        self.cantSkip[2][8] = self.cantSkip[4][6] = self.cantSkip[8][2] = self.cantSkip[6][4] = 5
        self.cantSkip[1][9] = self.cantSkip[9][1] = self.cantSkip[7][3] = self.cantSkip[3][7] = 5
        self.visited = [0 for _ in range(10)]
        self.cellTypes = [1, 2, 5]

    def validSelection(self, candidate, keyPadNum):
        canVisit = not self.visited[candidate]
        same = candidate == keyPadNum
        canSkipCenter = self.cantSkip[keyPadNum][candidate]
        canBeSkipped = not canSkipCenter or self.visited[canSkipCenter]
        return canVisit and canBeSkipped and not same

    def backtracking(self, keyPadNum, numberOfPresses, keyPressesNeeded):
        if numberOfPresses == keyPressesNeeded:
            return 1
        combinations = 0
        self.visited[keyPadNum] = 1
        for candidate in range(1, 10):
            if self.validSelection(candidate, keyPadNum):
                combinations += self.backtracking(candidate,
                                                  numberOfPresses + 1, keyPressesNeeded)
        self.visited[keyPadNum] = 0
        return combinations

    def numberOfPatterns(self, m: int, n: int) -> int:
        patterns = 0
        for keyPressesNeeded in range(m, n+1):
            cumulativeSum = 0
            for cell in self.cellTypes:
                result = self.backtracking(cell, 1, keyPressesNeeded)
                if cell != 5:
                    result = result + result + result + result
                cumulativeSum += result
            patterns += cumulativeSum
        return patterns


m = 1
n = 1
print(Solution().numberOfPatterns(m, n))
