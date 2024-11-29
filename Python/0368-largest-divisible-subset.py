# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [[]]
        for n in sorted(nums):
            dp.append(
                max((s + [n] for s in dp if not s or n % s[-1] == 0), key=len))
        return max(dp, key=len)


nums = [1, 2, 3]
print(Solution().largestDivisibleSubset(nums))
