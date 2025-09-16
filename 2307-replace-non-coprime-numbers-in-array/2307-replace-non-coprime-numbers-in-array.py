# time complexity: O(n^2 * logm)
# space complexity: O(n)
from math import gcd, lcm
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
                stack.append(lcm(stack.pop(), stack.pop()))
        return stack


nums = [6, 4, 3, 2, 7, 6, 2]
print(Solution().replaceNonCoprimes(nums))
nums = [2, 2, 1, 1, 3, 3, 3]
print(Solution().replaceNonCoprimes(nums))
