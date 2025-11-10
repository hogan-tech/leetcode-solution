# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        monoStack = [-1]
        result = 0
        for num in nums:
            while num < monoStack[-1]:
                monoStack.pop()
            if num > monoStack[-1]:
                result += (num > 0)
                monoStack.append(num)
        return result


nums = [0, 2]
print(Solution().minOperations(nums))
nums = [3, 1, 2, 1]
print(Solution().minOperations(nums))
nums = [1, 2, 1, 2, 1, 2]
print(Solution().minOperations(nums))
nums = [1, 0, 2, 0, 3]
print(Solution().minOperations(nums))
