# time complexity: O(nlogn)
# space complexity: O(n)
import bisect
from typing import List


class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        sortedAbs = sorted([abs(num) for num in nums])
        n = len(sortedAbs)
        result = 0
        for i in range(n):
            x = sortedAbs[i]
            maxY = 2 * x
            j = bisect.bisect_right(sortedAbs, maxY, i+1) - 1
            if j >= i + 1:
                result += j - i
        return result


nums = [0, 1, 2, 3]
print(Solution().perfectPairs(nums))
nums = [-3, 2, -1, 4]
print(Solution().perfectPairs(nums))
nums = [1, 10, 100, 1000]
print(Solution().perfectPairs(nums))
