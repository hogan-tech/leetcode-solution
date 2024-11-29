# time complexity: O(1)
# space complexity: O(n)
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(Solution().findDifference(nums1, nums2))
