# time complexity: O(n)
# space complexity: O(n)
from math import ceil
from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        avg = total / n
        if avg.is_integer():
            temp = int(avg) + 1
        else:
            temp = ceil(avg)

        if temp < 1:
            temp = 1

        numSet = set(nums)
        result = temp
        while True:
            if result not in numSet:
                return result
            result += 1


nums = [3, 5]
print(Solution().smallestAbsent(nums))
nums = [-1, 1, 2]
print(Solution().smallestAbsent(nums))
nums = [4, -1]
print(Solution().smallestAbsent(nums))
