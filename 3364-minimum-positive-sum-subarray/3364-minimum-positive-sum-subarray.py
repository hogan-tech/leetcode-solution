# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minSum = float('inf')
        found = False

        for size in range(l, r + 1):
            currentSum = sum(nums[:size])
            if currentSum > 0:
                minSum = min(minSum, currentSum)
                found = True

            for i in range(size, n):
                currentSum += nums[i] - nums[i - size]
                if currentSum > 0:
                    minSum = min(minSum, currentSum)
                    found = True

        return minSum if found else -1


nums = [3, -2, 1, 4]
l = 2
r = 3
print(Solution().minimumSumSubarray(nums, l, r))
nums = [-2, 2, -3, 1]
l = 2
r = 3
print(Solution().minimumSumSubarray(nums, l, r))
nums = [1, 2, 3, 4]
l = 2
r = 4
print(Solution().minimumSumSubarray(nums, l, r))
