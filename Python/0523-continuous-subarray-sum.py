# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderMap = {0: -1}
        cumulativeSum = 0

        for i, num in enumerate(nums):
            cumulativeSum += num
            remainder = cumulativeSum % k
            if remainder in remainderMap:
                if i - remainderMap[remainder] > 1:
                    return True
            else:
                remainderMap[remainder] = i

        return False


nums = [23, 2, 4, 6, 7]
k = 6
print(Solution().checkSubarraySum(nums, k))
