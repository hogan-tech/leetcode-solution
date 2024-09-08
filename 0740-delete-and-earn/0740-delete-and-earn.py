# time complexity: O(n+k)
# space complexity: O(n+k)
from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        maxNumber = 0
        for num in nums:
            points[num] += num
            maxNumber = max(maxNumber, num)

        @lru_cache
        def dp(num):
            if num == 0:
                return 0
            if num == 1:
                return points[1]

            return max(dp(num - 1), dp(num - 2) + points[num])

        return dp(maxNumber)


nums = [3, 4, 4, 2]
print(Solution().deleteAndEarn(nums))
