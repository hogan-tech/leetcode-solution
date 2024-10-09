# time complexity: O(n)
# space complexity: O(n)
class Solution:

    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0
        stack = []
        currNum = 0
        operation = "+"
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            if (not c.isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if operation == "-":
                    stack.append(-currNum)
                elif operation == "*":
                    stack.append(stack.pop() * currNum)
                elif operation == "+":
                    stack.append(currNum)
                else:
                    tmp = stack.pop()
                    if tmp // currNum < 0 and tmp % currNum != 0:
                        stack.append(tmp // currNum + 1)
                    else:
                        stack.append(tmp // currNum)
                operation = s[i]
                currNum = 0
        return sum(stack)


s = "3+2*2"
print(Solution().calculate(s))
