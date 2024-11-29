# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        minLength = float('inf')
        left = 0
        right = 0
        bitCounts = [0] * 32
        while right < len(nums):
            self.updateBitCounts(bitCounts, nums[right], 1)
            while (left <= right and self.converBitsToNum(bitCounts) >= k):
                minLength = min(minLength, right - left + 1)
                self.updateBitCounts(bitCounts, nums[left], -1)
                left += 1
            right += 1

        return -1 if minLength == float('inf') else minLength

    def updateBitCounts(self, bitCounts: list, number: int, delta: int) -> None:
        for pos in range(32):
            if number & (1 << pos):
                bitCounts[pos] += delta

    def converBitsToNum(self, bitCounts: list):
        result = 0
        for pos in range(32):
            if bitCounts[pos]:
                result |= 1 << pos
        return result


nums = [1, 2]
k = 0
print(Solution().minimumSubarrayLength(nums, k))
