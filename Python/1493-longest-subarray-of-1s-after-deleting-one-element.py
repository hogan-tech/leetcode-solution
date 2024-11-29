# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        zeros = 0
        result = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            result = max(result, right - left)
        return result


nums = [1, 1, 0, 1]
print(Solution().longestSubarray(nums))
