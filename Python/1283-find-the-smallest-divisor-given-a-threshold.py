# time complexity: O(nlogn)
# space complexity: O(1)
from math import ceil
import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left <= right:
            mid = (right + left) // 2
            count = 0
            for num in nums:
                count += math.ceil(num / mid)
            if threshold < count:
                left = mid + 1
            else:
                right = mid - 1
        return left


'''
9 + 5 + 7 + 3 + 1
'''

nums = [1, 2, 5, 9]
threshold = 6
print(Solution().smallestDivisor(nums, threshold))
nums = [44, 22, 33, 11, 1]
threshold = 5
print(Solution().smallestDivisor(nums, threshold))
