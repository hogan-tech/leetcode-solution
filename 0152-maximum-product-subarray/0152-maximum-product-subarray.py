# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        maxSoFar, minSoFar, result = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            tempMax = max(curr, max(maxSoFar * curr, minSoFar * curr))
            minSoFar = min(curr, min(maxSoFar * curr, minSoFar * curr))
            maxSoFar = tempMax
            result = max(result, maxSoFar)

        return result


nums = [-2, 0, -1]
print(Solution().maxProduct(nums))
