# time complexity: O(nlogn)
# space complexity: O(n)
import math
from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        result = set()
        for num in nums:
            squareRoot = int(math.sqrt(num))
            for primeNum in range(2, squareRoot + 1):
                if num % primeNum == 0:
                    result.add(primeNum)
                    while num % primeNum == 0:
                        num //= primeNum
            if num >= 2:
                result.add(num)
        return len(result)


nums = [2, 4, 3, 7, 10, 6]
print(Solution().distinctPrimeFactors(nums))
nums = [2, 4, 8, 16]
print(Solution().distinctPrimeFactors(nums))
