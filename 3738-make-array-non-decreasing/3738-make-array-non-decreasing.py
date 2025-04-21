# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []
        for x in nums:
            stack.append(x)
            while len(stack) >= 2 and stack[-2] > stack[-1]:
                mergeMaxValue = max(stack[-2], stack[-1])
                stack.pop()
                stack.pop()
                stack.append(mergeMaxValue)
        return len(stack)


nums = [4, 2, 5, 3, 5]
print(Solution().maximumPossibleSize(nums))
nums = [1, 2, 3]
print(Solution().maximumPossibleSize(nums))
