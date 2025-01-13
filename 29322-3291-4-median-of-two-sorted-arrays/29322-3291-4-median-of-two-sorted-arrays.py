# time complexity: O(log(min(m, n)))
# space complexity: O(1)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        left = 0
        right = m
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA
            maxLeftA = float(
                '-inf') if partitionA == 0 else nums1[partitionA - 1]
            minRightA = float('inf') if partitionA == m else nums1[partitionA]
            maxLeftB = float(
                '-inf') if partitionB == 0 else nums2[partitionB - 1]
            minRightB = float('inf') if partitionB == n else nums2[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1


nums1 = [1, 3]
nums2 = [2, 4]

print(Solution().findMedianSortedArrays(nums1, nums2))
