from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxNum = max(nums)
        count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == maxNum:
                count = max(count, right - left + 1)
            else:
                left = right + 1
        return count


nums = [311155, 311155, 311155, 311155, 311155,
        311155, 311155, 311155, 201191, 311155]
print(Solution().longestSubarray(nums))
