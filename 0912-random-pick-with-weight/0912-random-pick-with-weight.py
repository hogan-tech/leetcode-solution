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
            
# time complexity: O(logn)
# space complexity: O(n)
class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = []
        currSum = 0
        for i in range(len(w)):
            currSum += w[i]
            self.prefixSum.append(currSum)
        self.total = currSum

    def pickIndex(self) -> int:
        target = self.total * random.random()
        left = 0
        right = len(self.prefixSum)
        while left <= right:
            mid = (right + left) // 2
            if self.prefixSum[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left        


solution = Solution([1, 3])
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
