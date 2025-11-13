# time complexity: O(1)
# space complexity: O(1)
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


nums = [1, 2, 1]
print(Solution().getConcatenation(nums))
nums = [1, 3, 2, 1]
print(Solution().getConcatenation(nums))
