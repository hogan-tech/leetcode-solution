# time complexity: O(nlogn)
# space complexity: O(n)
import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minheap = sticks
        heapq.heapify(minheap)
        res = 0
        while len(minheap) > 1:
            v1 = heapq.heappop(minheap)
            v2 = heapq.heappop(minheap)
            temp = v1 + v2
            res += temp
            heapq.heappush(minheap, temp)
        return res


sticks = [2, 4, 3]
print(Solution().connectSticks(sticks))
