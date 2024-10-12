# time complexity: O(n)
# space complexty: O(1)
from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        total, previousUpper = 0, 0
        for upper, rate in brackets:
            upper = min(upper, income)
            total += (upper - previousUpper) * rate / 100
            previousUpper = upper

        return total


brackets = [[3, 50], [7, 10], [12, 25]]
income = 10
print(Solution().calculateTax(brackets, income))
