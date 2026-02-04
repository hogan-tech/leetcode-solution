# time complexity: O(n)
# space complexity: O(1)s
from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        result = float("-inf")
        i = 0

        while i < n:
            j = i + 1
            temp = 0

            while j < n and nums[j - 1] < nums[j]:
                j += 1
            p = j - 1

            if p == i:
                i += 1
                continue

            temp += nums[p] + nums[p - 1]
            while j < n and nums[j - 1] > nums[j]:
                temp += nums[j]
                j += 1
            q = j - 1

            if q == p or q == n - 1 or (j < n and nums[j] <= nums[q]):
                i = q
                continue

            temp += nums[q + 1]

            maxSum = 0
            currSum = 0
            k = q + 2
            while k < n and nums[k] > nums[k - 1]:
                currSum += nums[k]
                maxSum = max(maxSum, currSum)
                k += 1
            temp += maxSum

            maxSum = 0
            currSum = 0
            for k in range(p - 2, i - 1, -1):
                currSum += nums[k]
                maxSum = max(maxSum, currSum)
            temp += maxSum

            result = max(result, temp)
            i = q

        return result


nums = [0, -2, -1, -3, 0, 2, -1]
print(Solution().maxSumTrionic(nums))
nums = [1, 4, 2, 7]
print(Solution().maxSumTrionic(nums))
