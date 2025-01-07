# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        number = 0
        signValue = 1
        operationStack = []
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            if c in "+-":
                result += number * signValue
                signValue = 1 if c == '+' else -1
                number = 0
            elif c == '(':
                operationStack.append(result)
                operationStack.append(signValue)
                result = 0
                signValue = 1
            elif c == ')':
                result += signValue * number
                popSignValue = operationStack.pop()
                result *= popSignValue
                secondValue = operationStack.pop()
                result += secondValue
                number = 0

        return result + number * signValue


s = "1 + 1"
print(Solution().calculate(s))
s = " 2-1 + 2 "
print(Solution().calculate(s))
s = "(1+(4+5+2)-3)+(6+8)"
print(Solution().calculate(s))
