# time complexity: O(nlogk)
# space complexity: O(k)
from heapq import heapify, heappop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapify(maxHeap)
        while k:
            currNum = -heappop(maxHeap)
            k -= 1

        return currNum


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution().findKthLargest(nums, k))
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(Solution().findKthLargest(nums, k))
