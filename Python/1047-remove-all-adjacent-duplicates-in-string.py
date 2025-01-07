# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) == 0 or c != stack[-1]:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)


s = "abbaca"
print(Solution().removeDuplicates(s))
s = "azxxzy"
print(Solution().removeDuplicates(s))
