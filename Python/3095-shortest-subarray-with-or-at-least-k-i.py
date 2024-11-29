# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp |= nums[j]
                if temp >= k:
                    ans = min(ans, j-i+1)
                    break
        return ans if ans != float('inf') else -1


nums = [1, 2, 3]
k = 2
print(Solution().minimumSubarrayLength(nums, k))
