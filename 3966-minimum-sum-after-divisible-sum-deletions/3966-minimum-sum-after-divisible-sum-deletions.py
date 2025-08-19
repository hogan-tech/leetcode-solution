# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        dp = 0

        modMap = {0: 0}

        for num in nums:
            prefix = (prefix + num) % k

            dp += num

            if prefix in modMap:
                dp = min(dp, modMap[prefix])

            modMap[prefix] = min(modMap.get(prefix, float('inf')), dp)

        return dp


nums = [1, 1, 1]
k = 2
print(Solution().minArraySum(nums, k))
nums = [3, 1, 4, 1, 5]
k = 3
print(Solution().minArraySum(nums, k))
