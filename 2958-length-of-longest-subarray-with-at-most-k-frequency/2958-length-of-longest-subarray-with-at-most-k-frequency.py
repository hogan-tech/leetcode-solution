# time complexity: O(n)
# space complexity: O(n)
from collections import Counter
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans, start = 0, -1
        frequency = Counter()
        for end in range(len(nums)):
            frequency[nums[end]] += 1
            while frequency[nums[end]] > k:
                start += 1
                frequency[nums[start]] -= 1
            ans = max(ans, end - start)
        return ans


nums = [1, 2, 3, 1, 2, 3, 1, 2]
k = 2
print(Solution().maxSubarrayLength(nums, k))
