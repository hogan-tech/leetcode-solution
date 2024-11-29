# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flipped = [False] * len(nums)
        validFlipsFromPastWindow = 0
        flipCount = 0
        for i in range(len(nums)):
            if i >= k:
                if flipped[i - k]:
                    validFlipsFromPastWindow -= 1
            if validFlipsFromPastWindow % 2 == nums[i]:
                if i + k > len(nums):
                    return -1
                validFlipsFromPastWindow += 1
                flipped[i] = True
                flipCount += 1
        return flipCount


nums = [0, 1, 0]
k = 1
print(Solution().minKBitFlips(nums, k))
