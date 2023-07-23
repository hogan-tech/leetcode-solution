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
            if token in operations:
                number2 = stack.pop()
                number1 = stack.pop()
                operation = operations[token]
                result = operation(number1, number2)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]