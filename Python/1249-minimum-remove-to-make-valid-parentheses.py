# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexesToRemove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexesToRemove.add(i)
            else:
                stack.pop()
        indexesToRemove = indexesToRemove.union(set(stack))
        stringBuilder = []
        for i, c in enumerate(s):
            if i not in indexesToRemove:
                stringBuilder.append(c)
        return "".join(stringBuilder)


s = "lee(t(c)o)de)"
print(Solution().minRemoveToMakeValid(s))
