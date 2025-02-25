# time complexity: O(n)
# space complexity: O(1)
from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        prefixSumDict = defaultdict(lambda: float('inf'))
        result = -float('inf')
        for num in nums:
            if prefixSumDict[num] > prefixSum:
                prefixSumDict[num] = prefixSum
                
            prefixSum += num

            result = max(
                result, prefixSum - prefixSumDict[num + k], prefixSum - prefixSumDict[num - k])

        return result if result > -float('inf') else 0


nums = [1, 2, 3, 4, 5, 6]
k = 1
print(Solution().maximumSubarraySum(nums, k))
nums = [-1, 3, 2, 4, 5]
k = 3
print(Solution().maximumSubarraySum(nums, k))
nums = [-1, -2, -3, -4]
k = 2
print(Solution().maximumSubarraySum(nums, k))
