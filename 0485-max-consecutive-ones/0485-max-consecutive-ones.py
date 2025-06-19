# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            if num:
                count += 1
            else:
                count = 0
            result = max(result, count)
        return result


nums = [1, 1, 0, 1, 1, 1]
print(Solution().findMaxConsecutiveOnes(nums))
nums = [1, 0, 1, 1, 0, 1]
print(Solution().findMaxConsecutiveOnes(nums))
