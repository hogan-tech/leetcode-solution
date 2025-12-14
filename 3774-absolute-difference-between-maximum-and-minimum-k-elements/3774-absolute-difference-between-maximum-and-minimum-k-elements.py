# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        largest = 0
        smallest = 0
        n = len(nums)
        nums.sort()
        largest = sum(nums[n - k:])
        smallest = sum(nums[:k])
        return abs(largest - smallest)


nums = [5, 2, 2, 4]
k = 2
print(Solution().absDifference(nums, k))
nums = [100]
k = 1
print(Solution().absDifference(nums, k))
