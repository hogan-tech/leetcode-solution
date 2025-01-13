# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


nums = [0, 1, 0, 3, 2, 3]
print(Solution().lengthOfLIS(nums))
