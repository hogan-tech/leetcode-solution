# time complexity: O(m^2)
# space complexity: O(n^2)
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        memo = {}

        def dp(op, left):
            if op == m:
                return 0
            if (op, left) in memo:
                return memo[(op, left)]

            l = nums[left] * multipliers[op] + dp(op+1, left+1)
            r = nums[(n-1)-(op-left)] * multipliers[op] + dp(op+1, left)

            memo[(op, left)] = max(l, r)

            return memo[(op, left)]

        return dp(0, 0)


nums = [1, 2, 3]
multipliers = [3, 2, 1]
print(Solution().maximumScore(nums, multipliers))
