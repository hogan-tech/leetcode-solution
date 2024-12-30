# time complexity: O(logn)
# space complexity: O(1)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(Solution().search(nums, target))
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(Solution().search(nums, target))
nums = [3, 1]
target = 1
print(Solution().search(nums, target))
