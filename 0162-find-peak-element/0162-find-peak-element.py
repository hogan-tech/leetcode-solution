class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] <= nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left