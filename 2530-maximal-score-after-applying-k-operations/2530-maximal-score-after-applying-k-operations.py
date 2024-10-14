# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heappush(pq, -num)
        ans = 0
        for _ in range(k):
            maxNum = heappop(pq)
            ans += -maxNum
            heappush(pq, ceil(maxNum//3))
        return ans


nums = [1, 10, 3, 3, 3]
k = 3
print(Solution().maxKelements(nums, k))
