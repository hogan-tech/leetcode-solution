# time complexity: O(n)
# space complexity: O(1)
import math
from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        currSum = sum(nums)
        target = goal - currSum
        if target == 0:
            return 0
        if abs(target) <= limit:
            return 1
        else:
            return math.ceil(abs(target) / limit)


nums = [1, -1, 1]
limit = 3
goal = -4
print(Solution().minElements(nums, limit, goal))
nums = [1, -10, 9, 1]
limit = 100
goal = 0
print(Solution().minElements(nums, limit, goal))
nums = [-1, 0, 1, 1, 1]
limit = 1
goal = 771843707
print(Solution().minElements(nums, limit, goal))
