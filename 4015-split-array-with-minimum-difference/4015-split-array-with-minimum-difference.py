# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]

        suffix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] + nums[i]

        increasing = [True for _ in range(n)]
        decreasing = [True for _ in range(n)]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                increasing[i] = increasing[i-1]
            else:
                increasing[i] = False

        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                decreasing[i] = decreasing[i+1]
            else:
                decreasing[i] = False

        result = float("inf")
        found = False
        for i in range(n-1):
            if increasing[i] and decreasing[i+1]:
                leftSum = prefix[i]
                rightSum = suffix[i+1]
                result = min(result, abs(leftSum - rightSum))
                found = True

        return result if found else -1


nums = [1, 3, 2]
print(Solution().splitArray(nums))
nums = [1, 2, 4, 3]
print(Solution().splitArray(nums))
nums = [3, 1, 2]
print(Solution().splitArray(nums))
