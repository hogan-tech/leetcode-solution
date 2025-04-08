# time complexity: O(nlogn)
# space complexity: O(1)
from math import floor, sqrt
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            divisor = set()
            for i in range(1, floor(sqrt(num)) + 1):
                if num % i == 0:
                    divisor.add(i)
                    divisor.add(num // i)
                if len(divisor) > 4:
                    break
            if len(divisor) == 4:
                result += sum(divisor)
        return result


nums = [21, 4, 7]
print(Solution().sumFourDivisors(nums))
nums = [21, 21]
print(Solution().sumFourDivisors(nums))
nums = [1, 2, 3, 4, 5]
print(Solution().sumFourDivisors(nums))
