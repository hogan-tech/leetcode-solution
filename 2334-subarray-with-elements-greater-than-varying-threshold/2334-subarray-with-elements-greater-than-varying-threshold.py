# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(0)
        stack = [(0, -1)]
        for i, num in enumerate(nums):
            while len(stack) > 1 and num <= stack[-1][0]:
                if stack[-1][0] > threshold / (i - 1 - stack[-2][1]):
                    return i - 1 - stack[-2][1]
                stack.pop()
            stack.append((num, i))
        return -1


nums = [1, 3, 4, 3, 1]
threshold = 6
print(Solution().validSubarraySize(nums, threshold))
