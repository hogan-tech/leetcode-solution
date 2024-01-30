# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "*": lambda a, b: a*b,
            "/": lambda a, b: int(a/b),
        }
        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                operator = operations[token]
                stack.append(operator(num1, num2))
        return stack[0]


Tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(Tokens))
