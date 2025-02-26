# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefixSum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        maxOptiSumIdx = prefixSum.index(max(prefixSum))
        minNegSumIdx = prefixSum.index(min(prefixSum))

        minOptiSumIdx = prefixSum.index(min(prefixSum[:maxOptiSumIdx+1]))
        maxNegSumIdx = prefixSum.index(max(prefixSum[:minNegSumIdx+1]))

        result = max(abs(prefixSum[maxOptiSumIdx] - prefixSum[minOptiSumIdx]),
                     abs(prefixSum[minNegSumIdx]-prefixSum[maxNegSumIdx]))

        return result


nums = [1, -3, 2, 3, -4]
print(Solution().maxAbsoluteSum(nums))
nums = [2, -5, 1, -4, 3, -2]
print(Solution().maxAbsoluteSum(nums))
