# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        totalCount, currentSum = 0, 0
        freq = {}
        for num in nums:
            currentSum += num
            if currentSum == goal:
                totalCount += 1
            if currentSum - goal in freq:
                totalCount += freq[currentSum - goal]
            freq[currentSum] = freq.get(currentSum, 0) + 1

        return totalCount


nums = [1, 0, 1, 0, 1]
goal = 2
print(Solution().numSubarraysWithSum(nums, goal))
