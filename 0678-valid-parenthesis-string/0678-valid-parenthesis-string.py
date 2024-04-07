# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        starStack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == "*":
                starStack.append(i)
            else:
                if stack:
                    stack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        while stack and starStack:
            if stack.pop() > starStack.pop():
                return False
        return not stack


s = "(*))"
print(Solution().checkValidString(s))
