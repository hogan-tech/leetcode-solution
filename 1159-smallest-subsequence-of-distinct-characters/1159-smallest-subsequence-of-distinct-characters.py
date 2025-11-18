# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        seen = set()
        lastCharIdx = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < lastCharIdx[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)

        return ''.join(stack)


s = "bcabc"
print(Solution().smallestSubsequence(s))
s = "cbacdcbc"
print(Solution().smallestSubsequence(s))
