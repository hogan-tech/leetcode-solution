# time complexity: O(n)
# space complexity: O(min(n,k))
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, j in enumerate(nums):
            if j in dic and i - dic[j] <= k:
                return True
            dic[j] = i
        return False


nums = [1, 2, 3, 1]
k = 3
print(Solution().containsNearbyDuplicate(nums, k))
