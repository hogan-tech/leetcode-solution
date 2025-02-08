# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        prefixSum = 0
        result = 0
        pq = []
        for num in nums:
            if num < 0:
                heappush(pq, num)
            prefixSum += num
            if prefixSum < 0:
                prefixSum -= heappop(pq)
                result += 1
        return result


nums = [2, 3, -5, 4]
print(Solution().makePrefSumNonNegative(nums))
nums = [3, -5, -2, 6]
print(Solution().makePrefSumNonNegative(nums))
