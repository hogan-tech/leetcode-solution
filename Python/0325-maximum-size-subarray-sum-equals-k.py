# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        sumOfSubArray, maxSize = 0, 0
        rightDict = defaultdict(int)
        rightDict[0] = len(nums)

        for i in range(len(nums) - 1, -1, -1):

            sumOfSubArray += nums[i]
            if sumOfSubArray not in rightDict:
                rightDict[sumOfSubArray] = i

            complement = sumOfSubArray - k

            if complement in rightDict:
                maxSize = max(maxSize, rightDict[complement] - i)

        return maxSize


nums = [1, -1, 5, -2, 3]
k = 3
print(Solution().maxSubArrayLen(nums, k))
nums = [-2, -1, 2, 1]
k = 1
print(Solution().maxSubArrayLen(nums, k))
