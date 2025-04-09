# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        numSet = set()
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                numSet.add(num)
        return len(numSet)


nums = [5, 2, 5, 4, 5]
k = 2
print(Solution().minOperations(nums, k))
nums = [2, 1, 2]
k = 2
print(Solution().minOperations(nums, k))
nums = [9, 7, 5, 3]
k = 1
print(Solution().minOperations(nums, k))
