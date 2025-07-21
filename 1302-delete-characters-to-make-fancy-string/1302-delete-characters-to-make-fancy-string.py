# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 2:
            return s
        stack = [s[0], s[1]]
        for i in range(2, len(s)):
            if s[i] == stack[-1] and s[i] == stack[-2]:
                continue
            else:
                stack.append(s[i])
        return "".join(stack)


s = "leeetcode"
print(Solution().makeFancyString(s))
