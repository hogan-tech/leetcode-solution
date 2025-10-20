# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx1 = m - 1
        idx2 = n - 1
        currIdx = m + n - 1

        while idx2 >= 0:
            if idx1 >= 0 and nums1[idx1] > nums2[idx2]:
                nums1[currIdx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[currIdx] = nums2[idx2]
                idx2 -= 1
            currIdx -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(Solution().merge(nums1, m, nums2, n))
nums1 = [1]
m = 1
nums2 = []
n = 0
print(Solution().merge(nums1, m, nums2, n))
nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(Solution().merge(nums1, m, nums2, n))
