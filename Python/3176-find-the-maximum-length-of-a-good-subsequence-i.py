# time complexity: O(n^2*k)
# space complexity: O(n^2)
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1] * min(k + 1, 51) for _ in range(n)]
        maxLen = 1
        for i in range(1, n):
            for j in range(min(k, 50) + 1):
                for m in range(i):
                    if nums[m] == nums[i]:
                        dp[i][j] = max(dp[i][j], dp[m][j] + 1)
                    elif j > 0:
                        dp[i][j] = max(dp[i][j], dp[m][j-1] + 1)
                maxLen = max(maxLen, dp[i][j])
        return maxLen


nums = [1, 2, 1, 1, 3]
k = 2
print(Solution().maximumLength(nums, k))
