# time complexity: O(n*2^n)
# space complexity: O(2^n)
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        if len(expression) == 0:
            return result
        if len(expression) == 1:
            return [int(expression)]
        if len(expression) == 2 and expression[0].isdigit:
            return [int(expression)]
        for i, c in enumerate(expression):
            if c.isdigit():
                continue
            leftResults = self.diffWaysToCompute(expression[:i])
            rightResults = self.diffWaysToCompute(expression[i+1:])
            for leftResult in leftResults:
                for rightResult in rightResults:
                    if c == "+":
                        result.append(leftResult + rightResult)
                    elif c == "*":
                        result.append(leftResult * rightResult)
                    elif c == "-":
                        result.append(leftResult - rightResult)
        return result


expression = "2-1-1"
print(Solution().diffWaysToCompute(expression))
