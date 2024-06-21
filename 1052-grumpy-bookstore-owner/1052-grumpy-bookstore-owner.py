# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        curBenefit = sum(customers[:minutes])
        maxBenefit = curBenefit
        optimalStart = 0
        for start in range(1, len(customers) - minutes + 1):
            end = start + minutes - 1
            if grumpy[start-1] == 1:
                curBenefit -= customers[start-1]
            if grumpy[end] == 1:
                curBenefit += customers[end]
                if curBenefit > maxBenefit:
                    maxBenefit = curBenefit
                    optimalStart = start
        baseSatisfy = 0
        for i in range(len(customers)):
            if grumpy[i] == 0 or optimalStart <= i < optimalStart + minutes:
                baseSatisfy += customers[i]
        return baseSatisfy


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
print(Solution().maxSatisfied(customers, grumpy, minutes))
