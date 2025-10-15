# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {"(": ")", "[": "]", "{": "}"}
        openSet = set(["(", "[", "{"])
        stack = []
        for char in s:
            if char in openSet:
                stack.append(char)
            elif stack and char == bracketMap[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '{[(':
                stack.append(c)
            elif c == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif c == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        return len(stack) == 0

s = "()"
print(Solution().isValid(s))
s = "()[]{}"
print(Solution().isValid(s))
s = "(]"
print(Solution().isValid(s))
s = "([])"
print(Solution().isValid(s))
s = "([)]"
print(Solution().isValid(s))
