# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        shortestSubarrayLength = float("inf")
        cumulativeSum = 0
        prefixSumHeap = []
        for i, num in enumerate(nums):
            cumulativeSum += num
            if cumulativeSum >= k:
                shortestSubarrayLength = min(shortestSubarrayLength, i + 1)
            while (
                prefixSumHeap and cumulativeSum - prefixSumHeap[0][0] >= k
            ):
                shortestSubarrayLength = min(
                    shortestSubarrayLength, i - heappop(prefixSumHeap)[1]
                )
            heappush(prefixSumHeap, (cumulativeSum, i))

        return (
            -1
            if shortestSubarrayLength == float("inf")
            else shortestSubarrayLength
        )


nums = [1]
k = 1
print(Solution().shortestSubarray(nums, k))
nums = [1, 2]
k = 4
print(Solution().shortestSubarray(nums, k))
nums = [2, -1, 2]
k = 3
print(Solution().shortestSubarray(nums, k))
