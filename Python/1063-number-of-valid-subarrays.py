from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        mono = []
        size = len(nums)
        rightIndex = [size] * size
        for i in range(size):
            while mono and nums[mono[-1]] > nums[i]:
                idx = mono.pop(-1)
                rightIndex[idx] = i
            mono.append(i)
        res = 0
        for i in range(size):
            res += rightIndex[i] - i
        return res


nums = [1, 4, 2, 5, 3]
print(Solution().validSubarrays(nums))
