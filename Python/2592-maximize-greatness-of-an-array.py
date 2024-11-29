# time complexity: O(n)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        return len(nums) - max(Counter(nums).values())


nums = [1, 3, 5, 2, 1, 3, 1]
print(Solution().maximizeGreatness(nums))
