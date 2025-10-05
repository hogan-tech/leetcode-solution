# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xorAll = 0
        for num in nums:
            xorAll ^= num
        
        if xorAll != 0:
            return len(nums)
        
        if all(x == 0 for x in nums):
            return 0
        
        return len(nums) - 1


nums = [1, 2, 3]
print(Solution().longestSubsequence(nums))
nums = [2, 3, 4]
print(Solution().longestSubsequence(nums))
