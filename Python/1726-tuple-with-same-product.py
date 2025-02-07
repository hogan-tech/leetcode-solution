# time complexity: O(n^2)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        total = 0
        for i in range(n):
            for j in range(i + 1, n):
                value = nums[i] * nums[j]
                freq[value] += 1

        for value in freq.values():
            products = (value - 1) * value // 2
            total += products * 8

        return total


nums = [2, 3, 4, 6]
print(Solution().tupleSameProduct(nums))
nums = [1, 2, 4, 5, 10]
print(Solution().tupleSameProduct(nums))
