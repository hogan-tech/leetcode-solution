# time complexity: O(nlogn)
# space complexity: O(n)
import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = []
        for i in range(len(profits)):
            heapq.heappush(projects, (capital[i], profits[i]))

        available = []
        for _ in range(k):
            while projects and projects[0][0] <= w:
                heapq.heappush(available, -heapq.heappop(projects)[1])
            if len(available) == 0:
                break
            w -= heapq.heappop(available)
        return w


k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
print(Solution().findMaximizedCapital(k, w, profits, capital))
k = 3
w = 0
profits = [1, 2, 3]
capital = [0, 1, 2]
print(Solution().findMaximizedCapital(k, w, profits, capital))
