# time complexity: O(logn)
# space complexity: O(1)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        def BinarySearch(leftBoundary: int, rightBoundry: int, target: int):
            left, right = leftBoundary, rightBoundry
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                if nums[mid] > target:
                    right = mid - 1
                if nums[mid] == target:
                    return mid
            return -1

        if (ans := BinarySearch(0, left-1, target)) != -1:
            return ans
        return BinarySearch(left, len(nums) - 1, target)


Nums = [4, 5, 6, 7, 0, 1, 2, 3]
Target = 3
print(Solution().search(Nums, Target))
