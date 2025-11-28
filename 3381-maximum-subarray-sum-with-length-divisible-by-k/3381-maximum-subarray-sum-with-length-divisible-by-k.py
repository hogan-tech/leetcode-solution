# time complexity: O(n)
# space complexity: O(k)
from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        minS = [float('inf') for _ in range(k-1)]+[0]
        prefix, result = 0, float('-inf')
        for i, x in enumerate(nums):
            prefix += x
            iModK = i % k
            result = max(result, prefix-minS[iModK])
            minS[iModK] = min(prefix, minS[iModK])
        return result


nums = [1, 2]
k = 1
print(Solution().maxSubarraySum(nums, k))
nums = [-1, -2, -3, -4, -5]
k = 4
print(Solution().maxSubarraySum(nums, k))
nums = [-5, 1, 2, -3, 4]
k = 2
print(Solution().maxSubarraySum(nums, k))
