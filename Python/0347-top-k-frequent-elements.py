# time complexity: O(nlogk)
# space complexity: O(k)
from collections import Counter
from heapq import heappop, heappush
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        result = []
        for item, count in Counter(nums).items():
            heappush(maxHeap, (-count, item))

        while k:
            _, currItem = heappop(maxHeap)
            result.append(currItem)
            k -= 1

        return result


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
nums = [1]
k = 1
print(Solution().topKFrequent(nums, k))
