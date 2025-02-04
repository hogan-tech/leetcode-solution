# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = nums[0]
        tempSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                tempSum = nums[i]
            else:
                tempSum += nums[i]
            result = max(result, tempSum)
        return result


nums = [10, 20, 30, 5, 10, 50]
print(Solution().maxAscendingSum(nums))
nums = [10, 20, 30, 40, 50]
print(Solution().maxAscendingSum(nums))
nums = [12, 17, 15, 13, 10, 11, 12]
print(Solution().maxAscendingSum(nums))
