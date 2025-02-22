# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefixSum = [0 for _ in range(len(nums))]
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i - 1] + nums[i]

        result = -1
        minDiff = float('inf')
        for i in range(len(nums)):
            left = prefixSum[i] // (i + 1)
            right = (prefixSum[-1] - prefixSum[i]) // (len(nums) -
                                                       i - 1) if len(nums) - i - 1 != 0 else 0
            if minDiff > abs(left - right):
                minDiff = abs(left - right)
                result = i
        return result


nums = [2, 5, 3, 9, 5, 3]
print(Solution().minimumAverageDifference(nums))
nums = [0]
print(Solution().minimumAverageDifference(nums))
