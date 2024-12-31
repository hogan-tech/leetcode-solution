# time complexity: O(logn)
# space complexity: O(1)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        if len(nums) == 0:
            return False

        while left <= right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
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

        return False


nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
print(Solution().search(nums, target))
nums = [2, 5, 6, 0, 0, 1, 2]
target = 3
print(Solution().search(nums, target))
