# time complexity: O(1)
# space complexity: O(1)
import math
from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2
        b = int(math.floor(math.log2(n))) + 1
        return 1 << b


nums = [1, 2]
print(Solution().uniqueXorTriplets(nums))
nums = [3, 1, 2]
print(Solution().uniqueXorTriplets(nums))
