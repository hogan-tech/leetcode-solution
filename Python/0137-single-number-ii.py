# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        loner = 0
        for shift in range(32):
            bitSum = 0
            for num in nums:
                bitSum += (num >> shift) & 1
            lonerBit = bitSum % 3
            loner = loner | (lonerBit << shift)
        if loner >= (1 << 31):
            loner = loner - (1 << 32)
        return loner


nums = [0, 1, 0, 1, 0, 1, 99]
print(Solution().singleNumber(nums))
