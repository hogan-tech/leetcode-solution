from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left, ans = 0, 0
        minHeap, maxHeap = [], []
        heapify(minHeap)
        heapify(maxHeap)
        
        for right, num in enumerate( nums):
            while minHeap and (minHeap[0][1] < left or abs( minHeap[0][0] - num) > 2):
                _, idx = heappop(minHeap)
                left = max(idx + 1, left)
            while maxHeap and (maxHeap[0][1] < left or abs (-maxHeap[0][0] - num) > 2):
                _, idx = heappop(maxHeap)
                left = max(idx + 1,left)

            heappush(minHeap,[num,right])
            heappush(maxHeap,[-num,right])

            ans += right - left + 1
        return ans


nums = [5,4,2,4]
print(Solution().continuousSubarrays(nums))