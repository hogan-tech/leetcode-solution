# time complexity: O(n^2)
# space complexity: O(1)
from math import gcd
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n - ones
        result = float('inf')
        for left in range(n):
            temp = nums[left]
            for right in range(left + 1, n):
                temp = gcd(temp, nums[right])
                if temp == 1:
                    result = min(result, right - left)
        if result == float('inf'):
            return -1
        return result + n - 1


nums = [2, 6, 3, 4]
print(Solution().minOperations(nums))
nums = [2, 10, 6, 14]
print(Solution().minOperations(nums))
