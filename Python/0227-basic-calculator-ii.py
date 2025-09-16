# time complexity: O(n)
# space complexity: O(n)
import math


class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        prevOperation = '+'
        s += '+'
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ':
                pass
            else:
                if prevOperation == '+':
                    stack.append(num)
                elif prevOperation == '-':
                    stack.append(-num)
                elif prevOperation == '*':
                    operant = stack.pop()
                    stack.append((operant*num))
                elif prevOperation == '/':
                    operant = stack.pop()
                    stack.append(math.trunc(operant/num))
                num = 0
                prevOperation = c
        return sum(stack)


s = "3+2*2"
print(Solution().calculate(s))
s = " 3/2 "
print(Solution().calculate(s))
s = " 3+5 / 2 "
print(Solution().calculate(s))
