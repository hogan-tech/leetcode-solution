# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        result = 0
        buffer = 0
        for n in nums:
            buffer += n
            result |= n
            result |= buffer

        return result


nums = [2, 1, 0, 3]
print(Solution().subsequenceSumOr(nums))
