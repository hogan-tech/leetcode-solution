# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lowerBound = self.findBound(nums, target, True)
        if lowerBound == -1:
            return [-1, -1]
        upperBound = self.findBound(nums, target, False)
        return [lowerBound, upperBound]

    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                if isFirst:
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    right = mid - 1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


nums = [5, 7, 7, 8, 8, 10]
target = 6

print(Solution().searchRange(nums, target))
