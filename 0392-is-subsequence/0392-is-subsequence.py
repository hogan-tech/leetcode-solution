# time complexity: O(n)
# space complexity: O(n)
from collections import deque


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = deque()
        for c in s:
            queue.append(c)
        for c in t:
            if queue and c == queue[0]:
                queue.popleft()

        return len(queue) == 0


s = "abc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))
s = "axc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))
s = ""
t = "ahbgdc"
print(Solution().isSubsequence(s, t))
