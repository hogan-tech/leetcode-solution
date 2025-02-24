# time complexity: O(n*k)
# space complexity: O(n)
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack:
                prevC, prevCount = stack[-1]
                if prevC == c:
                    if prevCount + 1 == k:
                        while stack and stack[-1][0] == c:
                            stack.pop()
                    else:
                        stack.append((c, prevCount + 1))
                else:
                    stack.append((c, 1))
            else:
                stack.append((c, 1))

        words = [item[0] for item in stack]
        return ''.join(words)


s = "abcd"
k = 2
print(Solution().removeDuplicates(s, k))
s = "deeedbbcccbdaa"
k = 3
print(Solution().removeDuplicates(s, k))
s = "pbbcggttciiippooaais"
k = 2
print(Solution().removeDuplicates(s, k))
