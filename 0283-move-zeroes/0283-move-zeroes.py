# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0 and nums[left] == 0:
                nums[right], nums[left] = nums[left], nums[right]
            if nums[left] != 0:
                left += 1
        return nums