# time complexity: O(n^2)
# space complexity: O(1)
from math import gcd
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def lcm(a: int, b: int):
            return a*b // gcd(a, b)
        maxLen = 0
        n = len(nums)

        for left in range(n):
            prod = 1
            currGcd = nums[left]
            currLcm = nums[left]

            for right in range(left, n):
                prod *= nums[right]
                currGcd = gcd(currGcd, nums[right])
                currLcm = lcm(currLcm, nums[right])

                if prod == currLcm * currGcd:
                    maxLen = max(maxLen, right - left + 1)

        return maxLen


nums = [1, 2, 1, 2, 1, 1, 1]
print(Solution().maxLength(nums))
nums = [2, 3, 4, 5, 6]
print(Solution().maxLength(nums))
nums = [1, 2, 3, 1, 4, 5, 1]
print(Solution().maxLength(nums))
