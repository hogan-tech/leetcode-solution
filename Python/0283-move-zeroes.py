# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0 and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] != 0:
                left += 1
        print(nums)


'''
8 1 3 12 0 0 0
      1
             r
'''

nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))
nums = [0]
print(Solution().moveZeroes(nums))
