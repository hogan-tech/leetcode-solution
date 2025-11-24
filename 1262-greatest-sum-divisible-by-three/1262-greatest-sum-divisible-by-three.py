# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        A = sorted([x for x in nums if x % 3 == 1], reverse=True)
        B = sorted([x for x in nums if x % 3 == 2], reverse=True)
        total, remove = sum(nums), float("inf")

        if total % 3 == 0:
            remove = 0
        elif total % 3 == 1:
            if len(A) >= 1:
                remove = min(remove, A[-1])
            if len(B) >= 2:
                remove = min(remove, B[-2] + B[-1])
        else:
            if len(A) >= 2:
                remove = min(remove, A[-2] + A[-1])
            if len(B) >= 1:
                remove = min(remove, B[-1])

        return total - remove


nums = [3, 6, 5, 1, 8]
print(Solution().maxSumDivThree(nums))
nums = [4]
print(Solution().maxSumDivThree(nums))
nums = [1, 2, 3, 4, 4]
print(Solution().maxSumDivThree(nums))
