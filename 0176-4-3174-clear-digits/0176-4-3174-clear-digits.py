# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


s = "abc"
print(Solution().clearDigits(s))
s = "cb34"
print(Solution().clearDigits(s))
