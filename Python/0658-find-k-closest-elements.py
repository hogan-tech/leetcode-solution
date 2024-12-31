# time complexity: O(logn)
# space complexity: O(1)
from typing import List


class Solution:
    def findClosestElements(self, nums: List[int], k: int, target: int) -> List[int]:
        def binarySearch(nums: List[int], target: int) -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        if len(nums) == k:
            return nums
        if target <= nums[0]:
            return nums[:k]
        if nums[-1] <= target:
            return nums[len(nums) - k: len(nums)]

        firstCloset = binarySearch(nums, target)

        leftCloset = firstCloset - 1
        rightCloset = leftCloset + 1
        while (rightCloset - leftCloset - 1) < k:
            if leftCloset == -1:
                rightCloset += 1
                continue
            if rightCloset == len(nums) or abs(nums[leftCloset] - target) <= abs(nums[rightCloset] - target):
                leftCloset -= 1
            else:
                rightCloset += 1

        return nums[leftCloset + 1:rightCloset]


arr = [1, 2, 3, 4, 5]
k = 3
x = 4
print(Solution().findClosestElements(arr, k, x))
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(Solution().findClosestElements(arr, k, x))
arr = [1, 1, 2, 3, 4, 5]
k = 4
x = -1
print(Solution().findClosestElements(arr, k, x))
arr = [1, 2]
k = 1
x = 1
print(Solution().findClosestElements(arr, k, x))
