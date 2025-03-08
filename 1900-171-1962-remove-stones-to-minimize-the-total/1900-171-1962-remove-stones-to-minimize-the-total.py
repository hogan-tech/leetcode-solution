# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)
        while k > 0:
            currPile = -heappop(piles)
            newPile = currPile - (currPile // 2)
            heappush(piles, -newPile)
            k -= 1
        return -sum(piles)


piles = [5, 4, 9]
k = 2
print(Solution().minStoneSum(piles, k))
piles = [4, 3, 6, 7]
k = 3
print(Solution().minStoneSum(piles, k))
