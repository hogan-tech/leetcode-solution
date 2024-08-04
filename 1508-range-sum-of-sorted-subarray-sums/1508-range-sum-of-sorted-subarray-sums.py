# time complexity: O(n^2*logn)
# space complexity: O(n^2)
from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subList = []
        for i in range(len(nums)):
            tempSum = 0
            for j in range(i, len(nums)):
                tempSum += nums[j]
                subList.append(tempSum)
        subList.sort()
        ans = 0
        for i in range(left-1, right):
            mod = 10**9 + 7
            ans = (ans + subList[i]) % mod
        return ans


nums = [1, 2, 3, 4]
n = 4
left = 1
right = 10
print(Solution().rangeSum(nums, n, left, right))
