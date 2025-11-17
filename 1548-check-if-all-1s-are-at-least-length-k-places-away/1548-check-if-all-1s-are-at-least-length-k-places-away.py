# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def kLengthApart(self, nums:  List[int], k: int) -> bool:
        onesIdx = []
        for i, num in enumerate(nums):
            if num:
                onesIdx.append(i)
        for i in range(1, len(onesIdx)):
            if (onesIdx[i] - onesIdx[i - 1] - 1) < k:
                return False
        return True


nums = [1, 0, 0, 0, 1, 0, 0, 1]
k = 2
print(Solution().kLengthApart(nums, k))
nums = [1, 0, 0, 1, 0, 1]
k = 2
print(Solution().kLengthApart(nums, k))
