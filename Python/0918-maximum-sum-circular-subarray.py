from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]
        currMaxSum = 0
        currMinSum = 0
        totalSum = 0
        for num in nums:
            currMaxSum = max(currMaxSum, 0) + num
            maxSum = max(maxSum, currMaxSum)

            currMinSum = min(currMinSum, 0) + num
            minSum = min(minSum, currMinSum)

            totalSum += num
        
        if totalSum == minSum:
            return maxSum

        return max(maxSum, totalSum - minSum)


nums = [5, -3, 5]
print(Solution().maxSubarraySumCircular(nums))
