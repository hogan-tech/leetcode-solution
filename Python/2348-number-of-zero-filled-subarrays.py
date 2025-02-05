# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def calculateTotal(num):
            return (num + 1) * num // 2

        zeroCount = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
                if i == len(nums) - 1:
                    result += calculateTotal(zeroCount)
            else:
                result += calculateTotal(zeroCount)
                zeroCount = 0

        return result


nums = [1, 3, 0, 0, 2, 0, 0, 4]
print(Solution().zeroFilledSubarray(nums))
nums = [0, 0, 0, 2, 0, 0]
print(Solution().zeroFilledSubarray(nums))
nums = [2, 10, 2019]
print(Solution().zeroFilledSubarray(nums))
