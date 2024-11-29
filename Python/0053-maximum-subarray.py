# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = -100000
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum < nums[i]:
                sum = nums[i]
            maxNum = max(sum, maxNum)
        return maxNum


Nums = [5, 4, -1, 7, 8]

print(Solution().maxSubArray(Nums))
