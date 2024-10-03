# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        totalSum = 0
        for num in nums:
            totalSum = (totalSum + num) % p
        target = totalSum % p
        if target == 0:
            return 0

        modMap = {
            0: -1
        }
        currentSum = 0
        minLen = n
        for i in range(n):
            currentSum = (currentSum + nums[i]) % p
            needed = (currentSum - target + p) % p
            if needed in modMap:
                minLen = min(minLen, i - modMap[needed])
            modMap[currentSum] = i
        return -1 if minLen == n else minLen


nums = [3, 1, 4, 2]
p = 6
print(Solution().minSubarray(nums, p))
