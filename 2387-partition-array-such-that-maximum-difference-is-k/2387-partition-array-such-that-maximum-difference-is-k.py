# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], maxDiff: int) -> int:
        nums.sort()
        count = 1
        currMin = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - currMin > maxDiff:
                currMin = nums[i]
                count += 1
        return count


nums = [3, 6, 1, 2, 5]
k = 2
print(Solution().partitionArray(nums, k))
nums = [1, 2, 3]
k = 1
print(Solution().partitionArray(nums, k))
nums = [2, 2, 4, 5]
k = 0
print(Solution().partitionArray(nums, k))
