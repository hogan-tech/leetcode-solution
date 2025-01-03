# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxSoFar = nums[0]
        minSoFar = nums[0]
        result = maxSoFar
        for i in range(1, len(nums)):
            currNum = nums[i]
            preMax = maxSoFar
            maxSoFar = max(currNum, minSoFar * currNum, maxSoFar * currNum)
            minSoFar = min(currNum, minSoFar * currNum, preMax * currNum)
            result = max(result, maxSoFar)

        return result


nums = [2, 3, -2, 4]
print(Solution().maxProduct(nums))

nums = [-2, 0, -1]
print(Solution().maxProduct(nums))
