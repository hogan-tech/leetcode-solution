# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        windowSize = 2*k + 1
        result = [-1 for _ in range(len(nums))]
        if windowSize > len(nums):
            return result

        prefixSum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            prefixSum[i + 1] = nums[i] + prefixSum[i]

        for i in range(k, len(nums) - k):
            leftBound = i - k
            rightBound = i + k
            result[i] = (prefixSum[rightBound + 1] -
                         prefixSum[leftBound]) // windowSize

        return result


nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
k = 3
print(Solution().getAverages(nums, k))
nums = [100000]
k = 0
print(Solution().getAverages(nums, k))
nums = [8]
k = 100000
print(Solution().getAverages(nums, k))
