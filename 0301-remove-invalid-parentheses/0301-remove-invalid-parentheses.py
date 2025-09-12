# time complexity: O(2^n * n)
# space complexity: O(2^n * n)
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            stack = []
            for i in range(len(s)):
                if (s[i] == '('):
                    stack.append((i, '('))
                elif (s[i] == ')'):
                    if (stack and stack[-1][1] == '('):
                        stack.pop()
                    else:
                        stack.append((i, ')'))
            return len(stack) == 0, stack

        def backtrack(s, left, right):
            visited.add(s)
            if left == 0 and right == 0 and isValid(s)[0]:
                result.append(s)
            for i, char in enumerate(s):
                if char != '(' and char != ')':
                    continue
                if (char == '(' and left == 0) or (char == ')' and right == 0):
                    continue
                if s[:i] + s[i+1:] not in visited:
                    backtrack(s[:i] + s[i+1:], left -
                              (char == '('), right - (char == ')'))

        stack = isValid(s)[1]
        leftCount = sum([1 for val in stack if val[1] == "("])
        rightCount = len(stack) - leftCount

        result, visited = [], set()
        backtrack(s, leftCount, rightCount)
        return result


s = "()())()"
print(Solution().removeInvalidParentheses(s))
s = "(a)())()"
print(Solution().removeInvalidParentheses(s))
s = ")("
print(Solution().removeInvalidParentheses(s))
