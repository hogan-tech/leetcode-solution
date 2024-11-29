# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        par = list(range(n))

        def find(u):
            if u != par[u]:
                par[u] = find(par[u])
            return par[u]

        def join(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            if p1 > p2:
                par[p1] = p2
            else:
                par[p2] = p1
            return True

        logs.sort()
        for timestamp, x, y in logs:
            if join(x, y):
                n -= 1
            if n == 1:
                return timestamp
        return -1


logs = [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [
    20190224, 2, 4], [20190301, 0, 3], [20190312, 1, 2], [20190322, 4, 5]]
n = 6
print(Solution().earliestAcq(logs, n))
