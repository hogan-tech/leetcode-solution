# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumDigit(num):
            result = 0
            for c in num:
                result += int(c)
            return result

        for i, num in enumerate(nums):
            if i == sumDigit(str(num)):
                return i
        return -1


nums = [1, 3, 2]
print(Solution().smallestIndex(nums))
nums = [1, 10, 11]
print(Solution().smallestIndex(nums))
nums = [1, 2, 3]
print(Solution().smallestIndex(nums))
