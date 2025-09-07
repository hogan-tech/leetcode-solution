# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        L = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                L[i] = stack[-1]
            stack.append(i)

        R = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                R[i] = stack[-1]
            stack.append(i)

        result = 0
        for i in range(1, n-1):
            if L[i] != -1 and R[i] != n:
                if min(nums[L[i]], nums[R[i]]) > nums[i]:
                    result += 1
        return result


nums = [2, 5, 3, 1, 4]
print(Solution().bowlSubarrays(nums))
nums = [5, 1, 2, 3, 4]
print(Solution().bowlSubarrays(nums))
nums = [1000000000, 999999999, 999999998]
print(Solution().bowlSubarrays(nums))
nums = [1, 2, 3, 5, 4, 6]
print(Solution().bowlSubarrays(nums))
