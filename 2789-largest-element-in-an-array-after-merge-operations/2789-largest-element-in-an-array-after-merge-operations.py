class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        i = len(nums) - 2
        res = max(nums)
        while i >= 0:
            while i >= 0 and nums[i + 1] >= nums[i]:
                nums[i] += nums[i + 1]
                res = max(res, nums[i])
                i -= 1
            i -= 1
        return res