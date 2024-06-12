# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = curr = 0
        right = len(nums) - 1
        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1
            else:
                curr += 1
        return nums


nums = [1, 2, 0]
print(Solution().sortColors(nums))
