# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positiveNumsSet = set([num for num in nums if num > 0])
        return max(nums) if len(positiveNumsSet) == 0 else sum(positiveNumsSet)


nums = [1, 2, 3, 4, 5]
print(Solution().maxSum(nums))
nums = [1, 1, 0, 1, 1]
print(Solution().maxSum(nums))
nums = [1, 2, -1, -2, 1, 0, -1]
print(Solution().maxSum(nums))
nums = [2, -10, 6]
print(Solution().maxSum(nums))
