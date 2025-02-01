# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i-1] % 2 == nums[i] % 2:
                return False
        return True


nums = [1]
print(Solution().isArraySpecial(nums))
nums = [2, 1, 4]
print(Solution().isArraySpecial(nums))
nums = [4, 3, 1, 6]
print(Solution().isArraySpecial(nums))
