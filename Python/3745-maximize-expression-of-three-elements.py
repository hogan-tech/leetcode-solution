# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] + nums[-2] - nums[0]


nums = [1, 4, 2, 5]
print(Solution().maximizeExpressionOfThree(nums))
nums = [-2, 0, 5, -2, 4]
print(Solution().maximizeExpressionOfThree(nums))
