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