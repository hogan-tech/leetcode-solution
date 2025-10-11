# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        maxLen = 2
        currLen = 2
        for i in range(2, n):
            if nums[i] == nums[i - 1] + nums[i - 2]:
                currLen += 1
                maxLen = max(maxLen, currLen)
            else:
                currLen = 2

        return maxLen


nums = [1, 1, 1, 1, 2, 3, 5, 1]
print(Solution().longestSubarray(nums))
nums = [5, 2, 7, 9, 16]
print(Solution().longestSubarray(nums))
nums = [1000000000, 1000000000, 1000000000]
print(Solution().longestSubarray(nums))
