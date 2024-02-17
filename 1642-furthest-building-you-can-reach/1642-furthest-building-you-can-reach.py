# time complexity: O(nlogn)
# space complexity: O(min(n, l))
import heapq
from typing import List


class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        p = []
        i = 0
        for i in range(len(h) - 1):
            diff = h[i + 1] - h[i]
            if diff <= 0:
                continue
            b -= diff
            x = heapq.heappush(p, -diff)
            if b < 0:
                b += -heapq.heappop(p)
                l -= 1
            if l < 0:
                return i
        return len(h)-1


heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
bricks = 10
ladders = 2
print(Solution().furthestBuilding(heights, bricks, ladders))
