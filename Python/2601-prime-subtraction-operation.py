# time complexity: O(n+m*m^0.5)
# space complexity: O(m)
from math import isqrt
from typing import List


class Solution:
    def isprime(self, n):
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        maxElement = max(nums)
        previousPrime = [0] * (maxElement + 1)
        for i in range(2, maxElement + 1):
            if self.isprime(i):
                previousPrime[i] = i
            else:
                previousPrime[i] = previousPrime[i-1]
        for i in range(len(nums)):
            if i == 0:
                bound = nums[0]
            else:
                bound = nums[i] - nums[i-1]
            if bound <= 0:
                return False
            largestPrime = previousPrime[bound - 1]
            nums[i] -= largestPrime

        return True


nums = [4, 9, 6, 10]
print(Solution().primeSubOperation(nums))
