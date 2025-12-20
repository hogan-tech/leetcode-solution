# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List
import heapq


class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        n = len(nums)
        total = sum(nums)
        cap = 0
        maxHeap = []
        zeroSum = 0

        for i in range(n):
            if s[i] == '0':
                cap += 1
            zeroSum += nums[i]
            heapq.heappush(maxHeap, -nums[i])

            if len(maxHeap) > cap:
                removed = -heapq.heappop(maxHeap)
                zeroSum -= removed
        return total - zeroSum


nums = [2, 1, 5, 2, 3]
s = "01010"
print(Solution().maximumScore(nums, s))
nums = [4, 7, 2, 9]
s = "0000"
print(Solution().maximumScore(nums, s))
