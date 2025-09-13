# time complexity: O(n)
# spaec eomplexity: O(n)
from collections import deque
from typing import List


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        deques = {}
        result = 0
        n = len(arrivals)

        for i in range(n):
            t = arrivals[i]
            if t not in deques:
                deques[t] = deque()

            while deques[t] and deques[t][0] < i - w + 1:
                deques[t].popleft()

            if len(deques[t]) < m:
                deques[t].append(i)
            else:
                result += 1

        return result


arrivals = [1, 2, 1, 3, 1]
w = 4
m = 2
print(Solution().minArrivalsToDiscard(arrivals, w, m))
arrivals = [1, 2, 3, 3, 3, 4]
w = 3
m = 2
print(Solution().minArrivalsToDiscard(arrivals, w, m))
