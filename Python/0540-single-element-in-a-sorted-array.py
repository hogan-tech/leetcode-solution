# time complexity: O(logn)
# space complexity: O(1)
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left != right:
            mid = left + (right - left) // 2
            if mid % 2:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(Solution().singleNonDuplicate(nums))
nums = [3, 3, 7, 7, 10, 11, 11]
print(Solution().singleNonDuplicate(nums))
