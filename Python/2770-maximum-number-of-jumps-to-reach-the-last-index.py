# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp = [-1] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            if dp[i] == -1:
                continue
            for j in range(i+1, len(nums)):
                if -target <= nums[j] - nums[i] <= target:
                    dp[j] = max(dp[i] + 1, dp[j])
        return dp[-1] if dp[-1] else -1


nums = [1, 3, 6, 4, 1, 2]
target = 2
print(Solution().maximumJumps(nums, target))
nums = [1, 3, 6, 4, 1, 2]
target = 3
print(Solution().maximumJumps(nums, target))
nums = [1, 3, 6, 4, 1, 2]
target = 0
print(Solution().maximumJumps(nums, target))
nums = [0, 2, 1, 3]
target = 1
print(Solution().maximumJumps(nums, target))
