# time complexity: O(logn)
# space complexity: O(1)
from bisect import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]

# time complexity: O(logn)
# space complexity: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target) - 1
        if left < len(nums) and nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        first, last = -1, -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first = mid
                last = mid
                while first > 0 and nums[first - 1] == target:
                    first -= 1
                while last < len(nums) - 1 and nums[last + 1] == target:
                    last += 1
                return [first, last]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [first, last]


nums = [5, 7, 7, 8, 8, 10]
target = 6
print(Solution().searchRange(nums, target))
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(Solution().searchRange(nums, target))
nums = []
target = 0
print(Solution().searchRange(nums, target))
