# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        result = nums[0]

        for num in nums:
            vals = (num, num * currMin, num * currMax)
            currMin = min(vals)
            currMax = max(vals)
            result = max(result, currMax)

        return result


nums = [2, 3, -2, 4]
print(Solution().maxProduct(nums))
nums = [-2, 0, -1]
print(Solution().maxProduct(nums))
