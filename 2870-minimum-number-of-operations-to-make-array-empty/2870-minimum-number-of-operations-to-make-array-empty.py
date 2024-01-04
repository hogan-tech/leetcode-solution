from collections import Counter
from math import ceil
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dataSet = Counter(nums)
        sumOperations = 0
        for value in dataSet.values():
            if value == 1:
                return -1
            sumOperations += ceil(value / 3)
        return sumOperations


nums = [2, 1, 2, 2, 3, 3]
print(Solution().minOperations(nums))
