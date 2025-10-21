# time complexity: O(max(nlogn, klogn))
# space complexity: O(n)
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        result = 0
        numCount = {}
        lastNumIdx = 0
        for i in range(len(nums)):
            if nums[i] != nums[lastNumIdx]:
                numCount[nums[lastNumIdx]] = i - lastNumIdx
                result = max(result, i - lastNumIdx)
                lastNumIdx = i

        numCount[nums[lastNumIdx]] = len(nums) - lastNumIdx
        result = max(result, len(nums) - lastNumIdx)

        for i in range(nums[0], nums[-1] + 1):
            left = bisect_left(nums, i - k)
            right = bisect_right(nums, i + k) - 1
            if i in numCount:
                temp = min(right - left + 1, numCount[i] + numOperations)
            else:
                temp = min(right - left + 1, numOperations)
            result = max(result, temp)

        return result


nums = [1, 4, 5]
k = 2
numOperations = 2
print(Solution().maxFrequency(nums, k, numOperations))
nums = [5, 16, 20, 20, 20, 24, 24]
k = 5
numOperations = 4
print(Solution().maxFrequency(nums, k, numOperations))
nums = [2, 70, 73]
k = 39
numOperations = 2
print(Solution().maxFrequency(nums, k, numOperations))
