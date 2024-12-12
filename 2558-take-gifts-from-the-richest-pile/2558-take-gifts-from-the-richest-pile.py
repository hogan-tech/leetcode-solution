from heapq import heappop, heappush
from math import sqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        giftHeap = []
        for gift in gifts:
            heappush(giftHeap, -gift)

        for _ in range(k):
            currGift = -heappop(giftHeap)
            currGift = int(sqrt(currGift))
            heappush(giftHeap, -currGift)
        result = 0

        for num in giftHeap:
            result += -num

        return result


gifts = [25, 64, 9, 4, 100]
k = 4
print(Solution().pickGifts(gifts, k))
gifts = [1, 1, 1, 1]
k = 4
print(Solution().pickGifts(gifts, k))
