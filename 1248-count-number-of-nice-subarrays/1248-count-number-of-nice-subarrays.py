# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        currSum = 0
        subArrays = 0
        prefixSum = {currSum: 1}
        for i in range(len(nums)):
            currSum += nums[i] % 2
            if currSum - k in prefixSum:
                subArrays = subArrays + prefixSum[currSum - k]
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1

        return subArrays


nums = [1, 1, 2, 1, 1]
k = 3
print(Solution().numberOfSubarrays(nums, k))
