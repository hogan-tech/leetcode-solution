# time complexity: O(1)
# space complexity: O(1)
from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        num0 = bin(nums[0])[2:]
        num1 = bin(nums[1])[2:]
        num2 = bin(nums[2])[2:]
        result = max(int(num0 + num1 + num2, 2), int(num0 + num2 + num1, 2), int(num1 + num2 + num0, 2), int(num1 + num0 + num2, 2), int(num2 + num0 + num1, 2), int(num2 + num1 + num0, 2)
                     )

        return result


nums = [2, 8, 16]
print(Solution().maxGoodNumber(nums))
