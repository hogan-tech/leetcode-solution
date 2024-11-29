# time complexity: O(n^2)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        depth = 0
        visited, q = set(deadends), deque(["0000"])
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur == target:
                    return depth
                if cur not in visited:
                    q.extend(self.getNeighbors(cur))
                    visited.add(cur)
            depth += 1
        return -1

    def getNeighbors(self, s):
        res = []
        for i, c in enumerate(s):
            n = int(c)
            res.append(s[: i] + str((n - 1) % 10) + s[i + 1:])
            res.append(s[: i] + str((n + 1) % 10) + s[i + 1:])
        return res


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

print(Solution().openLock(deadends, target))
