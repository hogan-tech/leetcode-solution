# time complexity: O(n)
# space complexity: O(1)
from heapq import heapify, heappop
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxHeap = [-num for num in set(nums)]
        k = 3
        if len(maxHeap) < k:
            return -min(maxHeap)

        heapify(maxHeap)

        while k:
            currNum = -heappop(maxHeap)
            k -= 1
        return currNum


nums = [3, 2, 1]
print(Solution().thirdMax(nums))
nums = [1, 2]
print(Solution().thirdMax(nums))
nums = [2, 2, 3, 1]
print(Solution().thirdMax(nums))
