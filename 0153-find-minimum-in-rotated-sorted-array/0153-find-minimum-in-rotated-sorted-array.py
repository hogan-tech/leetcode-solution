# time complexity: O(logn)
# space complexity: O(1)
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[mid]


nums = [3, 4, 5, 1, 2]
print(Solution().findMin(nums))
nums = [4, 5, 6, 7, 0, 1, 2]
print(Solution().findMin(nums))
nums = [11, 13, 15, 17]
print(Solution().findMin(nums))
