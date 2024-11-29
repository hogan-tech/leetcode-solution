# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ans = float('inf')
        totalOne = sum(nums)

        oneCount = nums[0]
        end = 0
        for start in range(len(nums)):
            if start != 0:
                oneCount -= nums[start - 1]
            while end - start + 1 < totalOne:
                end += 1
                oneCount += nums[end % len(nums)]
            ans = min(ans, totalOne - oneCount)
        return ans


nums = [0, 1, 0, 1, 1, 0, 0]
print(Solution().minSwaps(nums))
