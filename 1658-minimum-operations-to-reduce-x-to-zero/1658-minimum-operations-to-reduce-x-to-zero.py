from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        maxI = -1
        left = 0
        current = 0

        for right in range(n):
            current += nums[right]
            while current > total - x and left <= right:
                current -= nums[left]
                left += 1
            if current == total - x:
                maxI = max(maxI, right - left + 1)

        return n - maxI if maxI != -1 else -1
