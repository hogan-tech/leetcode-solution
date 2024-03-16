# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sumVal = 0
        maxLen = 0
        for i, num in enumerate(nums):
            sumVal += 1 if num == 1 else -1
            if sumVal == 0:
                maxLen = i + 1
            elif sumVal in mp:
                maxLen = max(maxLen, i - mp[sumVal])
            else:
                mp[sumVal] = i
        return maxLen


nums = [0, 1, 0]
print(Solution().findMaxLength(nums))
