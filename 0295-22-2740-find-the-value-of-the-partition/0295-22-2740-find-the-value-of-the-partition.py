# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        result = float('inf')
        for i in range(1, len(nums)):
            result = min(result, abs(nums[i] - nums[i-1]))
        return result


nums = [1, 3, 2, 4]
print(Solution().findValueOfPartition(nums))
nums = [100, 1, 10]
print(Solution().findValueOfPartition(nums))
