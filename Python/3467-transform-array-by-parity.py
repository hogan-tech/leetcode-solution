# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] % 2:
                nums[i] = 1
            else:
                nums[i] = 0
        nums.sort()
        return nums


nums = [4, 3, 2, 1]
print(Solution().transformArray(nums))
nums = [1, 5, 1, 4, 2]
print(Solution().transformArray(nums))
