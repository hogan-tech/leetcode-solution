# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxResult = -1
        numsSet = {}
        for num in nums:
            if -num in numsSet:
                maxResult = max(maxResult, abs(num))
            numsSet[num] = -num
        return maxResult


nums = [-1, 10, 6, 7, -7, 1]
print(Solution().findMaxK(nums))
