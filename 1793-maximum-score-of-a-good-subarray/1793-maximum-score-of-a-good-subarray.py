from bisect import bisect_left
from cmath import inf
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def solve(nums, k):
            n = len(nums)
            left = [0] * k
            currMin = inf
            for i in range(k-1, -1, -1):
                currMin = min(nums[i], currMin)
                left[i] = currMin

            right = []
            currMin = inf
            for i in range(k, n):
                currMin = min(nums[i], currMin)
                right.append(currMin)

            ans = 0
            for j in range(len(right)):
                currMin = right[j]
                i = bisect_left(left, currMin)
                size = (k + j) - i + 1
                ans = max(ans, currMin * size)
            return ans
        return max(solve(nums, k), solve(nums[::-1], len(nums) - k - 1))


nums = [1, 4, 3, 7, 4, 5]
k = 3

print(Solution().maximumScore(nums, k))
