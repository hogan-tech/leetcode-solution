# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        left, right = [0] * n, [0] * n
        for currIdx in range(n):
            while stack and nums[stack[-1]] < nums[currIdx]:
                stack.pop()
            left[currIdx] = -1 if not stack else stack[-1]
            stack.append(currIdx)

        stack = []
        for currIdx in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[currIdx]:
                stack.pop()
            right[currIdx] = n if not stack else stack[-1]
            stack.append(currIdx)

        ans = [(right[currIdx] - left[currIdx] - 1) for currIdx in range(n)]
        return ans


nums = [1, 5, 4, 3, 6]
print(Solution().maximumLengthOfRanges(nums))
nums = [1, 2, 3, 4, 5]
print(Solution().maximumLengthOfRanges(nums))
