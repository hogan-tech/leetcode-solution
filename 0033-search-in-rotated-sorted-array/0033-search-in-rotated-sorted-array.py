from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return nums.index(target) if target in nums else -1
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        def binarySearch(left_boundary: int, right_boundary: int, target: int):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        if (answer := binarySearch(0, left-1, target)) != -1:
            return answer
        return binarySearch(left, n-1, target)


