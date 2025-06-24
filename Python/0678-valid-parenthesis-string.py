# time complexity: O(n)
# space complexity: O(n)
from functools import lru_cache


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

# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        @lru_cache(None)
        def dp(idx: int, openCount: int) -> bool:
            if idx == n:
                return openCount == 0
            if openCount < 0:
                return False
            if s[idx] == '*':
                return (
                    dp(idx + 1, openCount + 1) or
                    (openCount > 0 and dp(idx + 1, openCount - 1)) or
                    dp(idx + 1, openCount)
                )
            elif s[idx] == '(':
                return dp(idx + 1, openCount + 1)
            else:
                return openCount > 0 and dp(idx + 1, openCount - 1)

        return dp(0, 0)

# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        dp[n][0] = True

        for i in range(n - 1, -1, -1):
            for openCount in range(n):
                if s[i] == '(':
                    if openCount <= n - 1:
                        dp[i][openCount] = dp[i + 1][openCount + 1]
                elif s[i] == ')':
                    if openCount > 0:
                        dp[i][openCount] = dp[i + 1][openCount - 1]
                else:
                    result = False
                    if openCount <= n - 1:
                        result |= dp[i + 1][openCount + 1]
                    if openCount > 0:
                        result |= dp[i + 1][openCount - 1]
                    result |= dp[i + 1][openCount]
                    dp[i][openCount] = result
        return dp[0][0]

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount = 0
        closeCount = 0
        n = len(s)

        for left in range(n):
            right = n - 1 - left
            
            if s[left] == '(' or s[left] == '*':
                openCount += 1
            else:
                openCount -= 1

            if s[right] == ')' or s[right] == '*':
                closeCount += 1
            else:
                closeCount -= 1

            if openCount < 0 or closeCount < 0:
                return False

        return True


s = "()"
print(Solution().checkValidString(s))
s = "(*)"
print(Solution().checkValidString(s))
s = "(*))"
print(Solution().checkValidString(s))
