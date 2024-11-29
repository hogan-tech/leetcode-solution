# time complexity: O(max(m,n))
# space complexity: O(1)
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sumRolls = sum(rolls)
        remainingSum = mean * (n + len(rolls)) - sumRolls
        if remainingSum > 6 * n or remainingSum < n:
            return []
        distributeMean = remainingSum // n
        mod = remainingSum % n
        nElements = [distributeMean] * n
        for i in range(mod):
            nElements[i] += 1
        return nElements


rolls = [1, 2, 3, 4]
mean = 6
n = 4
print(Solution().missingRolls(rolls, mean, n))
