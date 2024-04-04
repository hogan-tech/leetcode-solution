class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxDepth = 0
        for c in s:
            if c == '(':
                depth += 1
                maxDepth = max(maxDepth, depth)
            elif c == ')':
                depth -= 1
        return maxDepth


s = "(1+(2*3)+((8)/4))+1"
print(Solution().maxDepth(s))
