# time complexity: O(n)
# space complexity: O(n)
from collections import Counter
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False

        freq = Counter(nums)
        maxGroups = n // k

        for count in freq.values():
            if count > maxGroups:
                return False

        return True


nums = [1, 2, 3, 4]
k = 2
print(Solution().partitionArray(nums, k))
nums = [3, 5, 2, 2]
k = 2
print(Solution().partitionArray(nums, k))
nums = [1, 5, 2, 3]
k = 3
print(Solution().partitionArray(nums, k))
