# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1 = float('inf')
        min2 = float('inf')

        for x in nums[1:]:
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x

        return nums[0] + min1 + min2


nums = [1, 2, 3, 12]
print(Solution().minimumCost(nums))
nums = [5, 4, 3]
print(Solution().minimumCost(nums))
nums = [10, 3, 1, 1]
print(Solution().minimumCost(nums))
