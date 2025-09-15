# time complexity: O(n)
# space complexity: O(n)
from collections import Counter
from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        majorityCount, majorityElement = max(
            (val, key) for key, val in Counter(nums).items())
        return majorityElement == target and majorityCount > len(nums) // 2


nums = [2, 4, 5, 5, 5, 5, 5, 6, 6]
target = 5
print(Solution().isMajorityElement(nums, target))
nums = [10, 100, 101, 101]
target = 101
print(Solution().isMajorityElement(nums, target))
