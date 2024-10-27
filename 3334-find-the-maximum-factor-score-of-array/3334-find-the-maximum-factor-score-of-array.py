# time complexity: O(n)
# space complexity: O(1)
from functools import reduce
from math import gcd, lcm
from typing import List


def gcdList(nums):
    return reduce(gcd, nums)


def lcmList(nums):
    return reduce(lambda x, y: lcm(x, y), nums)


class Solution:

    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] ** 2
        result = 0

        allGCD = gcdList(nums)
        allLCM = lcmList(nums)
        result = allGCD * allLCM

        for i in range(n):
            newNums = nums[:i] + nums[i+1:]
            if newNums:
                currGCD = gcdList(newNums)
                currLCM = lcmList(newNums)
                result = max(result, currGCD * currLCM)

        return result


print(Solution().maxScore([2, 4, 8, 16]))
print(Solution().maxScore([1, 2, 3, 4, 5]))
print(Solution().maxScore([3]))
