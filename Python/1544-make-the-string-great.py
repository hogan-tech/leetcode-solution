# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in list(s):
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


s = "leEeetcode"
print(Solution().makeGood(s))
