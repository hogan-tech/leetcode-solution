# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) - k + 1

        sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            sums.append(sums[-1] - nums[i-k] + nums[i])

        memo = [[-1] * 4 for _ in range(n)]
        indices = []

        self.dp(sums, k, 0, 3, memo)
        self.dfs(sums, k, 0, 3, memo, indices)

        return indices

    def dp(self, sums, k, idx, rem, memo):
        if rem == 0:
            return 0
        if idx >= len(sums):
            return float('-inf') if rem > 0 else 0
        if memo[idx][rem] != -1:
            return memo[idx][rem]

        withCurrent = sums[idx] + self.dp(sums, k, idx + k, rem - 1, memo)
        skipCurrent = self.dp(sums, k, idx + 1, rem, memo)

        memo[idx][rem] = max(withCurrent, skipCurrent)
        return memo[idx][rem]

    def dfs(self, sums, k, idx, rem, memo, indices):
        if rem == 0 or idx >= len(sums):
            return
        withCurrent = sums[idx] + self.dp(sums, k, idx + k, rem - 1, memo)
        skipCurrent = self.dp(sums, k, idx + 1, rem, memo)

        if withCurrent >= skipCurrent:
            indices.append(idx)
            self.dfs(sums, k, idx + k, rem - 1, memo, indices)
        else:
            self.dfs(sums, k, idx + 1, rem, memo, indices)


nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
print(Solution().maxSumOfThreeSubarrays(nums, k))
nums = [1, 2, 1, 2, 1, 2, 1, 2, 1]
k = 2
print(Solution().maxSumOfThreeSubarrays(nums, k))
