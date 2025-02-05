# time complexity: O(n!)
# space complexity: O(1)
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            for i in range(len(nums) - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            nums.pop()
        return nums[0]


nums = [1, 2, 3, 4, 5]
print(Solution().triangularSum(nums))
nums = [5]
print(Solution().triangularSum(nums))
