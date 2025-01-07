# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        result = list(s)
        for i in range(len(s)):
            if s[i] == ')':
                if len(stack) > 0 and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((')', i))
            if s[i] == '(':
                stack.append(('(', i))

        for item in stack:
            result[item[1]] = ""

        return "".join(result)


s = "lee(t(c)o)de)"
print(Solution().minRemoveToMakeValid(s))
s = "a)b(c)d"
print(Solution().minRemoveToMakeValid(s))
s = "))(("
print(Solution().minRemoveToMakeValid(s))
