# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heapify, heappop, heappush
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapify(maxHeap)
        score = 0
        while k:
            currNum = heappop(maxHeap)
            score += -currNum
            heappush(maxHeap, ceil(currNum // 3))
            k -= 1
        return score


nums = [10, 10, 10, 10, 10]
k = 5
print(Solution().maxKelements(nums, k))
nums = [1, 10, 3, 3, 3]
k = 3
print(Solution().maxKelements(nums, k))
