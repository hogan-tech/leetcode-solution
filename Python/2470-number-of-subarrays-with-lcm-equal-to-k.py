# time complexity: O(n^2 * logK)
# space complexity: O(1)
from typing import List


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def lcm(a, b):
            return a * b // gcd(a, b)

        count = 0
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i, len(nums)):
                temp = lcm(temp, nums[j])
                if temp == k:
                    count += 1
        return count


nums = [3, 6, 2, 7, 1]
k = 6
print(Solution().subarrayLCM(nums, k))
nums = [3]
k = 2
print(Solution().subarrayLCM(nums, k))
