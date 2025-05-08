# time complexity: O(n)
# space complexity: O(n)
from math import prod
from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        negNums = [i for i in nums if i < 0]
        posNums = [i for i in nums if i > 0]
        if not negNums and not posNums:
            return 0
        if len(negNums) % 2 == 1:
            negResult = prod(negNums[:-1]) if negNums[:-1] else 0
        else:
            negResult = prod(negNums)
        posResult = prod(posNums) if posNums else 0
        return max(negResult*posResult, posResult, negResult)


nums = [3, -1, -5, 2, 5, -9]
print(Solution().maxStrength(nums))
nums = [-4, -5, -4]
print(Solution().maxStrength(nums))
nums = [8, 6, 0, 5, -4, -8, -4, 9, -1, 6, -4, 8, -5]
print(Solution().maxStrength(nums))
