# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        targetCount = nums.count(k)
        maxGain = 0
        for i in range(1, 51):
            if i == k:
                continue
            currGain = 0
            maxCurr = 0
            for num in nums:
                if num == i:
                    currGain += 1
                elif num == k:
                    currGain -= 1
                currGain = max(currGain, 0)
                maxCurr = max(maxCurr, currGain)
            maxGain = max(maxGain, maxCurr)
        return targetCount + maxGain


nums = [1, 2, 3, 4, 5, 6]
k = 1
print(Solution().maxFrequency(nums, k))
nums = [10, 2, 3, 4, 5, 5, 4, 3, 2, 2]
k = 10
print(Solution().maxFrequency(nums, k))
nums = [1, 2, 1, 2, 5, 1]
k = 1
print(Solution().maxFrequency(nums, k))
