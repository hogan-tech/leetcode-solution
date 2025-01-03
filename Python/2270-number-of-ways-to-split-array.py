# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        prefixSum = [nums[0]] * n
        postfixSum = [nums[-1]] * n
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        for i in range(n - 2, -1, -1):
            postfixSum[i] = postfixSum[i + 1] + nums[i]
        for i in range(n - 1):
            if prefixSum[i] >= postfixSum[i + 1]:
                count += 1
        return count


nums = [10, 4, -8, 7]
print(Solution().waysToSplitArray(nums))
nums = [2, 3, 1, 0]
print(Solution().waysToSplitArray(nums))
