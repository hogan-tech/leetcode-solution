# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                return num


nums = [1, 2, 3, 3]
print(Solution().repeatedNTimes(nums))
nums = [2, 1, 2, 5, 3, 2]
print(Solution().repeatedNTimes(nums))
nums = [5, 1, 5, 2, 5, 3, 5, 4]
print(Solution().repeatedNTimes(nums))
nums = [9, 5, 3, 3]
print(Solution().repeatedNTimes(nums))
