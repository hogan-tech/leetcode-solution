# time complexity: O(n^3)
# space complexity: O(n^2)
from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        nums = [1] + nums + [1]

        @lru_cache(None)
        def dp(left, right):
            if right - left < 0:
                return 0
            result = 0
            for i in range(left, right + 1):
                gain = nums[left - 1] * nums[i] * nums[right + 1]
                remaining = dp(left, i - 1) + dp(i + 1, right)
                result = max(result, remaining + gain)
            return result

        return dp(1, len(nums) - 2)


nums = [3, 1, 5, 8]
print(Solution().maxCoins(nums))
