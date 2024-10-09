# time complexity: O(n)
# space complexity: O(n)
import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = []
        prefixSum = 0
        for weight in w:
            prefixSum += weight
            self.prefixSum.append(prefixSum)
        self.total = prefixSum

    def pickIndex(self) -> int:
        randomValue = self.total * random.random()
        for i in range(len(self.prefixSum)):
            if randomValue < self.prefixSum[i]:
                return i


solution = Solution([1, 3])
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
