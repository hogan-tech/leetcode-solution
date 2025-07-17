# time complexity: O(k^2 + nk)
# space complexity: O(k^2)
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        result = 0
        for num in nums:
            num %= k
            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                result = max(result, dp[prev][num])
        return result


nums = [1, 2, 3, 4, 5]
k = 2
print(Solution().maximumLength(nums, k))
nums = [1, 4, 2, 3, 1, 4]
k = 3
print(Solution().maximumLength(nums, k))
nums = [1, 2, 3, 10, 2]
k = 6
print(Solution().maximumLength(nums, k))
