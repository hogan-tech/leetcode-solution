from typing import List


class Solution:
    def evaluateExpr(self, stack):
        if not stack or type(stack[-1]) == str:
            stack.append(0)
        res = stack.pop()

        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res

    def calculate(self, s: str) -> int:
        stack = []
        n, operand = 0, 0
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch.isdigit():
                operand = (10 ** n * int(ch)) + operand
                n += 1
            elif ch != " ":
                if n:
                    stack.append(operand)
                    n, operand = 0, 0
                if ch == '(':
                    res = self.evaluateExpr(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(ch)
        if n:
            stack.append(operand)
        return self.evaluateExpr(stack)
