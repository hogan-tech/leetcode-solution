# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


nums = [2, 2, 1]
print(Solution().singleNumber(nums))
