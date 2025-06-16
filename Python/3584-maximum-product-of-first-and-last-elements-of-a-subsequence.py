# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)

        prefixMax = [-float('inf') for _ in range(n)]
        prefixMin = [float('inf') for _ in range(n)]

        suffixMax = [-float('inf') for _ in range(n)]
        suffixMin = [float('inf') for _ in range(n)]

        for i in range(n - m + 1):
            if i == 0:
                prefixMax[i] = nums[i]
                prefixMin[i] = nums[i]
            else:
                prefixMax[i] = max(prefixMax[i-1], nums[i])
                prefixMin[i] = min(prefixMin[i-1], nums[i])

        for i in range(n-1, m-2, -1):
            if i == n-1:
                suffixMax[i] = nums[i]
                suffixMin[i] = nums[i]
            else:
                suffixMax[i] = max(suffixMax[i+1], nums[i])
                suffixMin[i] = min(suffixMin[i+1], nums[i])

        result = -float('inf')
        for i in range(n - m + 1):
            j = i + m - 1
            if j >= n:
                continue
            result = max(
                result, prefixMax[i] * suffixMax[j], prefixMin[i] * suffixMin[j])

        return result


nums = [-1, -9, 2, 3, -2, -3, 1]
m = 1
print(Solution().maximumProduct(nums, m))
nums = [1, 3, -5, 5, 6, -4]
m = 3
print(Solution().maximumProduct(nums, m))
nums = [2, -1, 2, -6, 5, 2, -5, 7]
m = 2
print(Solution().maximumProduct(nums, m))
