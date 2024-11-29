# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


s = "erase*****"
print(Solution().removeStars(s))
