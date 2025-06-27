from typing import List

# time complexity: O(2^n)
# space complexity: O(n)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = 0
        
        def dfs(currIdx: int, currSum: int):
            nonlocal result
            if currIdx == len(nums):
                if currSum == target:
                    result += 1
            else:
                dfs(currIdx + 1, currSum + nums[currIdx])
                dfs(currIdx + 1, currSum - nums[currIdx])

        dfs(0, 0)
        return result

# bottom up
# time complexity: O(totalsum * n)
# space complexity: O(totalsum * n)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)
        if abs(target) > total:
            return 0
        dp = [[0] * (2 * total + 1) for _ in range(len(nums))]
        dp[0][nums[0] + total] = 1
        dp[0][-nums[0] + total] += 1
        for i in range(1, len(nums)):
            for itemSum in range(-total, total + 1):
                if (dp[i - 1][itemSum + total] > 0):
                    dp[i][itemSum + nums[i] + total] += dp[i-1][itemSum + total]
                    dp[i][itemSum - nums[i] + total] += dp[i-1][itemSum + total]
        return dp[len(nums) - 1][target + total]

# top down
# time complexity: O(totalsum * n)
# space complexity: O(totalsum * n)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        memo = [[float("-inf")] * (2 * totalSum + 1) for _ in range(len(nums))]

        def dfs(currIdx: int, currSum: int) -> int:
            if currIdx == len(nums):
                return 1 if currSum == target else 0
            else:
                if memo[currIdx][currSum + totalSum] != float("-inf"):
                    return memo[currIdx][currSum + totalSum]
                add = dfs(currIdx + 1, currSum + nums[currIdx])
                subtract = dfs(currIdx + 1, currSum - nums[currIdx],)
                memo[currIdx][currSum + totalSum] = add + subtract
                return memo[currIdx][currSum + totalSum]

        return dfs(0, 0)


nums = [1, 1, 1, 1, 1]
target = 3
print(Solution().findTargetSumWays(nums, target))
nums = [1]
target = 1
print(Solution().findTargetSumWays(nums, target))
