# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        curr = 1
        result = 0
        for num in nums:
            if num != curr:
                result += 1
                curr = num
        return result


nums = [0, 1, 1, 0, 1]
print(Solution().minOperations(nums))
nums = [1, 0, 0, 0]
print(Solution().minOperations(nums))
