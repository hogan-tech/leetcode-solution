# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        numsSet = set(nums)
        for i in range(max(nums) + k):
            if i + 1 not in numsSet:
                k -= 1
                if k == 0:
                    return i + 1
        return 0


arr = [2, 3, 4, 7, 11]
k = 5
print(Solution().findKthPositive(arr, k))
arr = [1, 2, 3, 4]
k = 2
print(Solution().findKthPositive(arr, k))
