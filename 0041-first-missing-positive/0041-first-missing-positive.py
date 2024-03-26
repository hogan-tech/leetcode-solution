# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        boolList = [False] * (n + 1)
        for num in nums:
            if 0 < num and num <= n:
                boolList[num] = True
        for i in range(1, n + 1):
            if not boolList[i]:
                return i
        return n + 1


nums = [3, 4, -1, 1]
print(Solution().firstMissingPositive(nums))
