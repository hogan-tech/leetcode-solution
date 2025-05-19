# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if abs(i - nums[i]) > 1:
                return False
        return True


nums = [1, 0, 2]
print(Solution().isIdealPermutation(nums))
nums = [1, 2, 0]
print(Solution().isIdealPermutation(nums))
nums = [3, 4, 0, 1, 2]
print(Solution().isIdealPermutation(nums))
