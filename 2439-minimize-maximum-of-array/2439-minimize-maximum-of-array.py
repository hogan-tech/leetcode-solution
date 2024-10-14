# time complexity: O(n)
# space complexity: O(1)
import math
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])

        ans = nums[0]
        print(prefixSum)
        for i, s in enumerate(prefixSum):
            ans = max(ans, int(math.ceil(s / (i + 1))))

        return ans


nums = [3, 7, 1, 6]
print(Solution().minimizeArrayValue(nums))
