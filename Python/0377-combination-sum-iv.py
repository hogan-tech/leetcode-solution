from functools import lru_cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def combs(remain: int):
            if remain == 0:
                return 1
            result = 0
            for num in nums:
                if remain - num >= 0:
                    result += combs(remain - num)
            return result
        return combs(target)


nums = [1, 2, 3]
target = 4
print(Solution().combinationSum4(nums, target))
