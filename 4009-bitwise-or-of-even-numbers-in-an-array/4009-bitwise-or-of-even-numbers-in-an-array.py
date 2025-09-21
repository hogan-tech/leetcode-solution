# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if num % 2 == 0:
                result |= num
        return result


nums = [1, 2, 3, 4, 5, 6]
print(Solution().evenNumberBitwiseORs(nums))
nums = [7, 9, 11]
print(Solution().evenNumberBitwiseORs(nums))
nums = [1, 8, 16]
print(Solution().evenNumberBitwiseORs(nums))
