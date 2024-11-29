# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixMod = 0
        modSeen = {0: -1}

        for i in range(len(nums)):
            prefixMod = (prefixMod + nums[i]) % k

            if prefixMod in modSeen:
                if i - modSeen[prefixMod] > 1:
                    return True
            else:
                modSeen[prefixMod] = i

        return False


nums = [23, 2, 4, 6, 7]
k = 6
print(Solution().checkSubarraySum(nums, k))
