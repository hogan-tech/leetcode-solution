# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result |= num
        return result << (len(nums) - 1)


nums = [1, 3]
print(Solution().subsetXORSum(nums))
