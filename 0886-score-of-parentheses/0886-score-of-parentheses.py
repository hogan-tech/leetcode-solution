# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        currLevel = 0
        for c in s:
            print(stack)
            if c == '(':
                stack.append(currLevel)
                currLevel = 0
            else:
                currLevel += stack.pop() + max(currLevel, 1)

        return currLevel


s = "()"
print(Solution().scoreOfParentheses(s))
s = "(())"
print(Solution().scoreOfParentheses(s))
s = "()()"
print(Solution().scoreOfParentheses(s))
