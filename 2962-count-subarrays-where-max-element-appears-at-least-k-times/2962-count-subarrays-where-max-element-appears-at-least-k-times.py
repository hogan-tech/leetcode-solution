# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        maxElement = max(nums)
        start = 0
        maxElementInWin = 0
        for i in range(len(nums)):
            if nums[i] == maxElement:
                maxElementInWin += 1
            while maxElementInWin == k:
                if nums[start] == maxElement:
                    maxElementInWin -= 1
                start += 1
            ans += start
        return ans


nums = [1, 3, 2, 3, 3]
k = 2

print(Solution().countSubarrays(nums, k))
