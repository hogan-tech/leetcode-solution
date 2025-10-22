# time complexity: O(nlogn)
# space complexity: O(n)
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        result = 0
        numFreq = defaultdict(int)
        modes = set()

        def addMode(value):
            modes.add(value)
            if value - k >= nums[0]:
                modes.add(value - k)
            if value + k <= nums[-1]:
                modes.add(value + k)

        lastNumIdx = 0
        for i in range(len(nums)):
            if nums[i] != nums[lastNumIdx]:
                numFreq[nums[lastNumIdx]] = i - lastNumIdx
                result = max(result, i - lastNumIdx)
                addMode(nums[lastNumIdx])
                lastNumIdx = i

        numFreq[nums[lastNumIdx]] = len(nums) - lastNumIdx
        result = max(result, len(nums) - lastNumIdx)
        addMode(nums[lastNumIdx])

        for mode in sorted(modes):
            left = bisect_left(nums, mode - k)
            right = bisect_right(nums, mode + k) - 1
            if mode in numFreq:
                temp = min(right - left + 1, numFreq[mode] + numOperations)
            else:
                temp = min(right - left + 1, numOperations)
            result = max(result, temp)

        return result


nums = [1, 4, 5]
k = 1
numOperations = 2
print(Solution().maxFrequency(nums, k, numOperations))
nums = [5, 11, 20, 20]
k = 5
numOperations = 1
print(Solution().maxFrequency(nums, k, numOperations))
