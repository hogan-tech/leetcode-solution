# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        numsSum = 0
        for i in range(k):
            numsSum += nums[i]
        result = numsSum
        for i in range(k, len(nums)):
            numsSum += (nums[i] - nums[i-k])
            result = max(result, numsSum)
        return result / k


nums = [5]
k = 1
print(Solution().findMaxAverage(nums, k))
