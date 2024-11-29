# time complexity: O(n+m)
# space complexity: O(n+m)
from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        unionNums = set(nums1).intersection(set(nums2))
        return min(unionNums) if unionNums else -1


nums1 = [1, 2, 3, 6]
nums2 = [2, 3, 4, 5]
print(Solution().getCommon(nums1, nums2))
