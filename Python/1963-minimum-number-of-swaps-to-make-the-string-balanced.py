# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        count = 0
        for c in s:
            if c == '[':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1
        return (count + 1) // 2


s = "[]"
print(Solution().minSwaps(s))
