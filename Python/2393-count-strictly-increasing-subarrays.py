from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        left = prev = count = 0
        for right in range(len(nums)):
            if prev >= nums[right]:
                left = right
            count += right - left + 1
            prev = nums[right]
        return count
    

nums = [1,3,5,4,4,6]
print(Solution().countSubarrays(nums))