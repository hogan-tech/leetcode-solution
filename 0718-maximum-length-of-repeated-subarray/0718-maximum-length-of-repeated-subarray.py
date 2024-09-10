# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    memo[i][j] = memo[i+1][j+1] + 1
        return max(max(row)for row in memo)


nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7]
print(Solution().findLength(nums1, nums2))
