# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr, left = 0, 0
        ans = 0
        for right in range(len(nums)):
            target = nums[right]
            curr += target

            while (right - left + 1) * target-curr > k:
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


nums = [1, 2, 4]
k = 5

print(Solution().maxFrequency(nums, k))
