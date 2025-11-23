# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        S = n * (n + 1) // 2
        if (S - target) < 0 or (S - target) % 2 != 0:
            return []
        sumPNeg = (S - target) // 2
        if sumPNeg < 0 or sumPNeg > S:
            return []
        pNeg = set()
        currSum = 0

        for i in range(n, 0, -1):
            if currSum + i <= sumPNeg:
                pNeg.add(i)
                currSum += i
        if currSum != sumPNeg:
            return []
        pNegList = sorted(list(pNeg), reverse=True)
        pPosSet = set(range(1, n + 1)) - pNeg
        pPosList = sorted(list(pPosSet), reverse=True)
        result = []
        for _ in range(n):
            candidateNeg = float('inf')
            if pNegList:
                candidateNeg = -pNegList[0]
            candidatePos = float('inf')
            if pPosList:
                candidatePos = pPosList[-1]
            if candidateNeg <= candidatePos:
                result.append(candidateNeg)
                pNegList.pop(0)
            else:
                result.append(candidatePos)
                pPosList.pop()
        return result


n = 3
target = 0
print(Solution().lexSmallestNegatedPerm(n, target))
n = 1
target = 10000000000
print(Solution().lexSmallestNegatedPerm(n, target))
