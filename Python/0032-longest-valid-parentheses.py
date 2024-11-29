# time complexity; O(n)
# space complexity: O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        stack.append(-1)
        count = 0
        for i, c in enumerate(s):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    count = max(count, i - stack[-1])
        return count


s = ")()())"
print(Solution().longestValidParentheses(s))
