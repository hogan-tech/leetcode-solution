# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        final = stack[:-k] if k else stack
        return "".join(final).lstrip('0') or "0"


num = "1432219"
k = 3

print(Solution().removeKdigits(num, k))
